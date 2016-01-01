# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20160101_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='portion',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(help_text='Например, "Чай и кофе"', max_length=256, default='', verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='desc_ru',
            field=models.TextField(verbose_name='Описание (рус.)', help_text='Например, "Хачапури в форме лодочки . Начинкой из сулугуни и сырого яйца"', max_length=4096, default='', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(help_text='Например, "Хачапури по аджарски"', max_length=256, default='', verbose_name='Название (рус.)'),
        ),
        migrations.AddField(
            model_name='product',
            name='portion_ru',
            field=models.CharField(help_text='Например, "300 гр."', max_length=128, default='', verbose_name='Порция (рус.)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(help_text='Например, "Чай"', max_length=256, default='', verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(help_text='Например, "Tea and coffee"', max_length=256, default='', verbose_name='Название (англ.)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc_en',
            field=models.TextField(verbose_name='Описание (англ.)', help_text='Например, "Khachapuri in the shape of a small boat with a Suluguni cheese"', max_length=4096, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(help_text='Например, "Adjarian khachapuri"', max_length=256, default='', verbose_name='Название (англ.)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='portion_en',
            field=models.CharField(help_text='Например, "300 gr."', max_length=128, default='', verbose_name='Порция (англ.)'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(help_text='Например, "Tea"', max_length=256, default='', verbose_name='Название (англ.)'),
        ),
    ]
