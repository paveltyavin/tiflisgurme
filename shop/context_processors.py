from django.conf import settings
from django.utils.timezone import now, make_naive
from shop.models import Phone

WEEKDAY_DICT = {
    0: 'понедельник',
    1: 'вторник',
    2: 'среда',
    3: 'четверг',
    4: 'пятница',
    5: 'суббота',
    6: 'воскресенье',
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
    result['open_text'] = 'Мы открыты !' if 12 <= n.hour < 22 else 'Мы закрыты.'
    result['LANGUAGE_CODE'] = settings.LANGUAGE_CODE

    return result
