from django.conf.urls import url
from shop.api import views

urlpatterns = [
    url(r'^product/(?P<pk>\d+)/$', views.ProductView.as_view(), name='product'),
]