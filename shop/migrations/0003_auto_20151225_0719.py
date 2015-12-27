# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_homeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Название', max_length=256)),
                ('image', models.ImageField(verbose_name='Изображение', upload_to=shop.models.convert_file_name)),
                ('ordering', models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'ordering': ('ordering',),
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.AlterField(
            model_name='homeimage',
            name='image',
            field=models.ImageField(verbose_name='Изображение', upload_to=shop.models.convert_file_name),
        ),
    ]
