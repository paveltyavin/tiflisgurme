from django.conf.urls import url, include
from shop import views

urlpatterns = [
    url(r'^test/error/$', views.test_error),
    url(r'^test/mail/$', views.test_mail),
    url(r'^$', views.StubView.as_view()),
    url(r'^home/$', views.HomeView.as_view()),
    url(r'^menu/$', views.MenuView.as_view()),
    url(r'^vacancy/$', views.VacancyView.as_view()),
    url(r'^news/$', views.NewsView.as_view()),
    url(r'^shipping/$', views.ShippingView.as_view()),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^contact/success/$', views.ContactSuccessView.as_view(), name='contact-success'),
]
