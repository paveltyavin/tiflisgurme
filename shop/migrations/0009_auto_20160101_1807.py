# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20160101_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовое', max_length=256)),
                ('text', models.TextField(default='', verbose_name='Текст')),
                ('ordering', models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')),
                ('image', models.ImageField(default='', upload_to=shop.models.convert_file_name, verbose_name='Изображение')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'ordering': ('ordering',),
                'verbose_name_plural': 'Новости',
                'verbose_name': 'Новость',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(default='', max_length=4096, blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to=shop.models.convert_file_name, blank=True, verbose_name='Изображение'),
        ),
    ]
