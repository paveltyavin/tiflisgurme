from django.conf import settings
from django.utils.timezone import now, make_naive
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _
from shop.models import Phone


def get_week_day(i):
    if i == 0:
        return _('monday')
    if i == 1:
        return _('tuesday')
    if i == 2:
        return _('wednesday')
    if i == 3:
        return _('thursday')
    if i == 4:
        return _('friday')
    if i == 5:
        return _('saturday')
    if i == 6:
        return _('sunday')


def get_open_text(hour):
    return _('We are open') if 12 <= hour < 22 else _('We are closed')


def get_phone_list():
    return Phone.objects.all()


def base(request):
    result = {
        'DEBUG': settings.DEBUG,
        'now': now,
        'phone_list': get_phone_list
    }

    n = make_naive(now())

    result['weekday'] = get_week_day(n.weekday())
    result['open_text'] = get_open_text(n.hour)
    result['LANGUAGE_CODE'] = get_language()
    return result
