# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20151226_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('value', models.CharField(max_length=256, verbose_name='Значение')),
                ('ordering', models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)),
            ],
            options={
                'verbose_name': 'Телефон',
                'ordering': ('ordering',),
                'verbose_name_plural': 'Телефоны',
            },
        ),
    ]
