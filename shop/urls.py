from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^contact/success/$', views.ContactSuccessView.as_view(), name='contact-success'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^menu/$', views.MenuView.as_view(), name='menu'),
    url(r'^menu/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^news/$', views.NewsView.as_view(), name='news'),
    url(r'^news/(?P<pk>\d+)/$', views.NewsDetailView.as_view(), name='news-detail'),
    url(r'^shipping/$', views.ShippingView.as_view(), name='shipping'),
    url(r'^vacancy/$', views.VacancyView.as_view(), name='vacancy'),
    url(r'^$', views.StubView.as_view(), name='stub'),
]
