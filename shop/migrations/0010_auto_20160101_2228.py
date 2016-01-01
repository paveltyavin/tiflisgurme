# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20160101_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(default='', verbose_name='Название (англ.)', max_length=256),
        ),
        migrations.AddField(
            model_name='product',
            name='desc_en',
            field=models.TextField(default='', verbose_name='Описание (англ.)', blank=True, max_length=4096),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(default='', verbose_name='Название (англ.)', max_length=256),
        ),
        migrations.AddField(
            model_name='product',
            name='portion',
            field=models.CharField(default='', verbose_name='Порция', max_length=128),
        ),
        migrations.AddField(
            model_name='product',
            name='portion_en',
            field=models.CharField(default='', verbose_name='Порция (англ.)', max_length=128),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(default='', verbose_name='Название (англ.)', max_length=256),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', verbose_name='Название', max_length=256),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='title',
            field=models.CharField(default='', verbose_name='Заголовок', max_length=256),
        ),
    ]
