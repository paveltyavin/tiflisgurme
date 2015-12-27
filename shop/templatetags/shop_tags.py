# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def active(request, pattern):
    import re

    if re.search(pattern, request.path):
        return 'active'
    return ''
