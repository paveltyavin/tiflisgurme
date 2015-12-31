# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='', verbose_name='Название', max_length=256)),
                ('ordering', models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')),
                ('image', models.ImageField(verbose_name='Изображение', upload_to=shop.models.convert_file_name)),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'ordering': ('ordering',),
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'ordering': ('ordering',), 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='category',
            name='kind',
            field=models.CharField(default='table', verbose_name='Тип отображения', max_length=10, choices=[('table', 'Таблица'), ('menu', 'Меню')]),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=None, blank=True, verbose_name='Категория', null=True, to='shop.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(default='', verbose_name='Описание', max_length=4096),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', verbose_name='Изображение', upload_to=shop.models.convert_file_name),
        ),
        migrations.AddField(
            model_name='product',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', verbose_name='Название', max_length=256),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(to='shop.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default=None, blank=True, verbose_name='Подкатегория', null=True, to='shop.SubCategory'),
        ),
    ]
