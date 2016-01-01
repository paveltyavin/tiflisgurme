from urllib.parse import urlsplit, urljoin
from django.conf import settings
from django.utils.timezone import now, make_naive
from django.utils.translation import get_language
from django.utils.translation import ugettext as _
from shop.models import Phone

WEEKDAY_DICT = {
    0: _('monday'),
    1: _('tuesday'),
    2: _('wednesday'),
    3: _('thursday'),
    4: _('friday'),
    5: _('saturday'),
    6: _('sunday'),
}


def get_phone_list():
    return Phone.objects.all()


def base(request):
    result = {
        'DEBUG': settings.DEBUG,
        'now': now,
        'phone_list': get_phone_list
    }

    n = make_naive(now())

    result['weekday'] = WEEKDAY_DICT[n.weekday()]
    result['open_text'] = _('We are open') if 12 <= n.hour < 22 else _('We are closed')
    result['LANGUAGE_CODE'] = get_language()
    return result
