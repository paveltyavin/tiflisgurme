from __future__ import unicode_literals
from django.contrib.admin import site
from django.contrib.admin.options import ModelAdmin
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


class NewsAdmin(ModelAdmin):
    list_display = ('title', 'ordering')
    list_editable = ('ordering',)


site.register(models.Vacancy, StandardAdmin)
site.register(models.Product, StandardAdmin)
site.register(models.Category, StandardAdmin)
site.register(models.SubCategory, StandardAdmin)
site.register(models.NewsItem, NewsAdmin)

site.register(models.Phone, PhoneAdmin)
site.register(models.HomeImage, HomeImageAdmin)

site.unregister(Group)
site.unregister(User)
