import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SECRET_KEY = 'change_me'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'proj.urls'
WSGI_APPLICATION = 'proj.wsgi.application'
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TEMPLATE_DIRS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop',
    'sorl.thumbnail',
    'django_extensions',
    'bootstrap3',
    'rest_framework',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "shop.context_processors.base",
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/dist'),
]

DATE_INPUT_FORMATS = ('%d.%m.%Y',)
TIME_INPUT_FORMATS = ('%H:%M',)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

THUMBNAIL_ENGINE = 'shop.pil_engine.MyEngine'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = 'mail@tiflisgurme.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'mail@tiflisgurme.com'