from django.conf.urls import url, include
from shop import views

urlpatterns = [
    url(r'api/', include('shop.api.urls', namespace='api')),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^contact/success/$', views.ContactSuccessView.as_view(), name='contact-success'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^menu/$', views.MenuView.as_view(), name='menu'),
    url(r'^menu/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^news/$', views.NewsView.as_view(), name='news'),
    url(r'^robots\.txt$', views.robots_view, name='robots'),
    url(r'^humans\.txt$', views.humans_view, name='humans'),
    url(r'^shipping/$', views.ShippingView.as_view(), name='shipping'),
    url(r'^test/error/$', views.test_error, name='test-error'),
    url(r'^test/mail/$', views.test_mail, name='test-mail'),
    url(r'^vacancy/$', views.VacancyView.as_view(), name='vacancy'),
    url(r'^$', views.StubView.as_view(), name='stub'),
]
