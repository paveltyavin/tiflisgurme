from __future__ import unicode_literals
from django.contrib.admin import site
from django.contrib.admin.options import ModelAdmin, InlineModelAdmin, TabularInline
from django.contrib.auth.models import Group, User
from shop import models


class StandardAdmin(ModelAdmin):
    list_display = ('name', 'ordering')
    list_editable = ('ordering',)


class HomeImageAdmin(ModelAdmin):
    list_display = ('image', 'ordering')
    list_editable = ('ordering',)


class PhoneAdmin(ModelAdmin):
    list_display = ('value', 'ordering')
    list_editable = ('ordering',)


class NewsImageInline(TabularInline):
    model = models.NewsImage
    extra = 0


class NewsAdmin(ModelAdmin):
    list_display = ('title', 'ordering')
    list_editable = ('ordering',)
    inlines = [NewsImageInline, ]


class TextBlockAdmin(ModelAdmin):
    list_display = ('name',)


class ProductAdmin(ModelAdmin):
    list_display = ('name', 'ordering', 'price')
    list_editable = ('ordering', 'price',)
    list_filter = ('category',)
    fields = (
        ('name_ru', 'name_en'),
        ('desc_ru', 'desc_en'),
        ('portion_ru', 'portion_en'),

        'price',
        'category',
        'sub_category',
        'image',
    )


site.register(models.Vacancy, StandardAdmin)
site.register(models.Product, ProductAdmin)
site.register(models.Category, StandardAdmin)
site.register(models.SubCategory, StandardAdmin)
site.register(models.NewsItem, NewsAdmin)
site.register(models.TextBlock, TextBlockAdmin)

site.register(models.Phone, PhoneAdmin)
site.register(models.HomeImage, HomeImageAdmin)

site.unregister(Group)
site.unregister(User)
