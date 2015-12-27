# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to=shop.models.convert_file_name)),
                ('ordering', models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)),
            ],
            options={
                'verbose_name': 'Изображение на главной',
                'verbose_name_plural': 'Изображения на главной',
                'ordering': ('ordering',),
            },
        ),
    ]
