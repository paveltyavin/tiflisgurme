# -*- coding: utf-8 -*-
import random
from django.db import models


def convert_file_name(instance, filename):
    ext = filename.split('.')[-1].lower()
    dirname = instance._meta.model_name
    name = ''.join(random.choice('0123456789') for _ in range(5))
    return '{}/{}.{}'.format(dirname, name, ext)


class Product(models.Model):
    name = models.CharField(max_length=256, default='')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


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


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to=convert_file_name, verbose_name='Изображение')
    ordering = models.PositiveSmallIntegerField(verbose_name='Сортировка', default=0)

    def __str__(self):
        if self.image:
            return self.image.url
        else:
            return ''

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
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
