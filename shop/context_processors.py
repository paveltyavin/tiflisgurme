from django.conf import settings
from django.utils.timezone import now


def base(request):
    return {
        'DEBUG': settings.DEBUG,
        'now': now
    }
