from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^test/error/$', views.test_error, name='test-error'),
    url(r'^test/mail/$', views.test_mail, name='test-mail'),
    url(r'^$', views.StubView.as_view(), name='stub'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^menu/$', views.MenuView.as_view(), name='menu'),
    url(r'^menu/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^vacancy/$', views.VacancyView.as_view(), name='vacancy'),
    url(r'^news/$', views.NewsView.as_view(), name='news'),
    url(r'^shipping/$', views.ShippingView.as_view(), name='shipping'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^contact/success/$', views.ContactSuccessView.as_view(), name='contact-success'),
]
