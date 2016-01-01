# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib.parse import urljoin, urlsplit
from django import template
from django.utils.translation import get_language
from shop.models import TextBlock

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
    return getattr(obj, "value_{}".format(get_language()))


@register.simple_tag
def change_lang(request, lang):
    path = request.path
    url_list = path.split('/')
    if url_list[0] == '':
        url_list = url_list[1:]
    url_list = url_list[1:]
    url = '/'.join(url_list)
    return urljoin('/{}/'.format(lang), url)
