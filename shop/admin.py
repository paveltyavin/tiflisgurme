from __future__ import unicode_literals
from django.contrib.admin import site
from django.contrib.auth.models import Group, User
from shop.models import Product, HomeImage, Phone

site.register(Phone)
site.register(Product)
site.register(HomeImage)
site.unregister(Group)
site.unregister(User)
