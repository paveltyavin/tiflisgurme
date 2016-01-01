# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20151231_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='image',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(to='shop.Category', verbose_name='Категория'),
        ),
    ]
