# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20160101_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256, verbose_name='Название', default='')),
                ('slug', models.SlugField(max_length=256, verbose_name='Идентификатор', default='')),
                ('value_ru', models.TextField(verbose_name='Текст (рус.)', default='')),
                ('value_en', models.TextField(verbose_name='Текст (англ.)', default='')),
            ],
            options={
                'verbose_name': 'Текстовый блок',
                'verbose_name_plural': 'Текстовые блоки',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Укажите, на странице какой категории будет отображаться этот товар. Если этот товар принадлежит какой-нибудь подкатегори, это поле заполнять не нужно', to='shop.Category', verbose_name='Категория', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, help_text='Укажите, в какой подкатегории должен отображаться этот товар. Это необязательное поле', to='shop.SubCategory', verbose_name='Подкатегория', default=None, null=True),
        ),
    ]
