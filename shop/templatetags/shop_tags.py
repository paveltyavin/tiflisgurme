# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib.parse import urljoin, urlsplit
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
from shop.models import TextBlock, Cart

register = template.Library()


@register.simple_tag
def active(request, pattern):
    import re

    if re.search(pattern, request.path):
        return 'active'
    return ''


@register.simple_tag
def text_block(slug):
    try:
        obj = TextBlock.objects.get(slug=slug)
    except TextBlock.DoesNotExist:
        return ''
    s = getattr(obj, "value_{}".format(get_language()))
    return mark_safe(s)


@register.simple_tag
def change_lang(request, lang):
    path = request.path
    url_list = path.split('/')
    if url_list[0] == '':
        url_list = url_list[1:]
    url_list = url_list[1:]
    url = '/'.join(url_list)
    return urljoin('/{}/'.format(lang), url)


@register.simple_tag
def get_cart_quantity(request, product):
    if hasattr(request, 'cartproduct_list'):
        cartproduct_list = request.cartproduct_list
    else:
        try:
            cart = Cart.objects.get(id=request.session['cart_id'])
            cartproduct_list = list(cart.cartproduct_set.all())
        except (KeyError, Cart.DoesNotExist):
            cartproduct_list = []
        request.cartproduct_list = cartproduct_list

    for cp in cartproduct_list:
        if cp.product_id == product.id:
            return cp.quantity
    return 0
