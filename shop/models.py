import random
from django.db import models
from django.conf import settings
from django.utils.translation import get_language
from sorl.thumbnail.shortcuts import get_thumbnail


def convert_file_name(instance, filename):
    ext = filename.split('.')[-1].lower()
    dirname = instance._meta.model_name
    name = ''.join(random.choice('0123456789') for _ in range(5))
    return '{}/{}.{}'.format(dirname, name, ext)


class Category(models.Model):
    name_ru = models.CharField(
        max_length=256,
        default='',
        verbose_name='Название',
        help_text='Например, "Чай и кофе"',
    )
    name_en = models.CharField(
        max_length=256,
        verbose_name='Название (англ.)',
        default='',
        help_text='Например, "Tea and coffee"',
    )

    image = models.ImageField(
        upload_to=convert_file_name,
        verbose_name='Изображение',
        default='',
        blank=True,
    )
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)
    kind = models.CharField(
        max_length=10,
        verbose_name='Тип отображения',
        choices=(
            ('table', 'Таблица'),
            ('menu', 'Меню'),
        ),
        default='table',
        help_text='',
    )

    @property
    def name(self):
        return getattr(self, 'name_{}'.format(get_language()))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ('ordering',)


class SubCategory(models.Model):
    name_ru = models.CharField(
        max_length=256,
        default='',
        verbose_name='Название',
        help_text='Например, "Чай"',
    )
    name_en = models.CharField(
        max_length=256,
        verbose_name='Название (англ.)',
        default='',
        help_text='Например, "Tea"',
    )

    category = models.ForeignKey('shop.Category', verbose_name='Категория')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)

    @property
    def name(self):
        return getattr(self, 'name_{}'.format(get_language()))

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ('ordering',)

    def __str__(self):
        return self.name


class Product(models.Model):
    name_ru = models.CharField(
        max_length=256,
        default='',
        verbose_name='Название (рус.)',
        help_text='Например, "Хачапури по аджарски"',
    )
    desc_ru = models.TextField(
        max_length=4096,
        default='',
        verbose_name='Описание (рус.)',
        blank=True,
        help_text='Например, "Хачапури в форме лодочки . Начинкой из сулугуни и сырого яйца"',
    )
    portion_ru = models.CharField(
        verbose_name='Порция (рус.)',
        max_length=128,
        default='',
        help_text='Например, "300 гр."',
    )

    name_en = models.CharField(
        max_length=256,
        default='',
        verbose_name='Название (англ.)',
        help_text='Например, "Adjarian khachapuri"',
    )
    desc_en = models.TextField(
        max_length=4096,
        default='',
        verbose_name='Описание (англ.)',
        blank=True,
        help_text='Например, "Khachapuri in the shape of a small boat with a Suluguni cheese"',
    )
    portion_en = models.CharField(
        max_length=128,
        verbose_name='Порция (англ.)',
        default='',
        help_text='Например, "300 gr."',
    )

    price = models.IntegerField(default=0, verbose_name='Цена')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)
    category = models.ForeignKey(
        'shop.Category',
        default=None,
        blank=True,
        null=True,
        verbose_name='Категория',
        help_text='Укажите, на странице какой категории будет отображаться этот товар. '
                  'Если этот товар принадлежит какой-нибудь подкатегори, это поле заполнять не нужно',
    )
    sub_category = models.ForeignKey(
        'shop.SubCategory',
        default=None,
        blank=True,
        null=True,
        verbose_name='Подкатегория',
        help_text='Укажите, в какой подкатегории должен отображаться этот товар. Это необязательное поле',
    )
    image = models.ImageField(upload_to=convert_file_name, verbose_name='Изображение', default='', blank=True)

    @property
    def name(self):
        return getattr(self, 'name_{}'.format(get_language()))

    @property
    def desc(self):
        return getattr(self, 'desc_{}'.format(get_language()))

    @property
    def portion(self):
        return getattr(self, 'portion_{}'.format(get_language()))

    def get_thumb(self):
        if self.image is None:
            return None
        try:
            t = get_thumbnail(self.image, 'x250')
        except IOError:
            return None
        if t:
            return t.url
        else:
            return None

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('ordering',)

    def __str__(self):
        return self.name


class HomeImage(models.Model):
    image = models.ImageField(upload_to=convert_file_name, verbose_name='Изображение')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)

    def __str__(self):
        if self.image:
            return self.image.url
        else:
            return ''

    class Meta:
        verbose_name = 'Изображение на главной'
        verbose_name_plural = 'Изображения на главной'
        ordering = ('ordering',)


class Phone(models.Model):
    value = models.CharField(max_length=256, verbose_name='Значение')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ('ordering',)

    def __str__(self):
        return self.value or 'телефон'


class Vacancy(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст', default='')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ('ordering',)

    def __str__(self):
        return self.name or 'вакансия'


class NewsItem(models.Model):
    title_ru = models.CharField(max_length=256, verbose_name='Заголовок (рус.)', default='')
    text_ru = models.TextField(verbose_name='Текст (рус.)', default='')
    title_en = models.CharField(max_length=256, verbose_name='Заголовок (англ.)', default='')
    text_en = models.TextField(verbose_name='Текст (англ.)', default='')

    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)
    image = models.ImageField(upload_to=convert_file_name, verbose_name='Изображение', default='')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('ordering',)

    @property
    def title(self):
        return getattr(self, 'title_{}'.format(get_language()))

    @property
    def text(self):
        return getattr(self, 'text_{}'.format(get_language()))

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    newsitem = models.ForeignKey('NewsItem')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)
    image = models.ImageField(upload_to=convert_file_name, verbose_name='Изображение', default='')

    class Meta:
        verbose_name = 'Изображение новости'
        verbose_name_plural = 'Изображения новостей'
        ordering = ('ordering',)

    def __str__(self):
        return str(self.ordering)


class TextBlock(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название', default='')
    slug = models.SlugField(max_length=256, verbose_name='Идентификатор', default='')
    value_ru = models.TextField(verbose_name='Текст (рус.)', default='')
    value_en = models.TextField(verbose_name='Текст (англ.)', default='')

    @property
    def value(self):
        return getattr(self, 'value_{}'.format(get_language()))

    class Meta:
        verbose_name = 'Текстовый блок'
        verbose_name_plural = 'Текстовые блоки'

    def __str__(self):
        return self.name


class Cart(models.Model):
    created = models.DateField(auto_now_add=True)

    def total_price(self):
        return sum(cp.product.price * cp.quantity for cp in self.cartproduct_set.all())

    def total_quantity(self):
        return sum(cp.quantity for cp in self.cartproduct_set.all())


class CartProduct(models.Model):
    product = models.ForeignKey('Product')
    cart = models.ForeignKey('Cart')
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'cart',)
