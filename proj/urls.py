from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from shop import views

urlpatterns = []
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('shop.api.urls', namespace='api')),
    url(r'^robots\.txt$', views.robots_view, name='robots'),
    url(r'^humans\.txt$', views.humans_view, name='humans'),
    url(r'^test/error/$', views.test_error, name='test-error'),
    url(r'^test/mail/$', views.test_mail, name='test-mail'),
]

urlpatterns += i18n_patterns(
    url(r'^', include('shop.urls')),
)
