from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = []
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('shop.urls')),
]
