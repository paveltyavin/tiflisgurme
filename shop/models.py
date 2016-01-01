# -*- coding: utf-8 -*-
import random
from django.db import models


def convert_file_name(instance, filename):
    ext = filename.split('.')[-1].lower()
    dirname = instance._meta.model_name
    name = ''.join(random.choice('0123456789') for _ in range(5))
    return '{}/{}.{}'.format(dirname, name, ext)


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to=convert_file_name, verbose_name='Изображение')
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ('ordering',)


class SubCategory(models.Model):
    name = models.CharField(max_length=256, default='', verbose_name='Название')
    category = models.ForeignKey('shop.Category', verbose_name='Категория')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ('ordering',)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, default='', verbose_name='Название')
    desc = models.TextField(max_length=4096, default='', verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)
    category = models.ForeignKey('shop.Category', default=None, blank=True, null=True,
                                 verbose_name='Категория', )
    sub_category = models.ForeignKey('shop.SubCategory', default=None, blank=True, null=True,
                                     verbose_name='Подкатегория', )
    image = models.ImageField(upload_to=convert_file_name, verbose_name='Изображение', default='')

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
