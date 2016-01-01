from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect
from django.utils.timezone import now, make_naive
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from shop.models import HomeImage, Category, Vacancy, NewsItem
from django.utils.translation import ugettext as _


class StubView(TemplateView):
    template_name = 'stub.html'


WEEKDAY_DICT = {
    0: _('monday'),
    1: _('tuesday'),
    2: _('wednesday'),
    3: _('thursday'),
    4: _('friday'),
    5: _('saturday'),
    6: _('sunday'),
}


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['home_image_list'] = HomeImage.objects.all()
        n = make_naive(now())

        ctx['weekday'] = WEEKDAY_DICT[n.weekday()]
        ctx['open_text'] = _('We are open') if 12 <= n.hour < 22 else _('We are closed')
        return ctx


class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category_list'] = Category.objects.all()
        return ctx


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            category = Category.objects.get(id=kwargs.get('pk'))
        except Category.DoesNotExist:
            raise Http404
        ctx['category'] = category
        ctx['category_list'] = Category.objects.all()
        ctx['product_without_sc'] = category.product_set.filter(sub_category__isnull=True)
        return ctx


class ShippingView(TemplateView):
    template_name = 'shipping.html'


class VacancyView(ListView):
    template_name = 'vacancy.html'
    model = Vacancy


class NewsView(ListView):
    template_name = 'news.html'
    model = NewsItem


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    model = NewsItem

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['newsitem_list'] = NewsItem.objects.all()
        return ctx


class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': _('Name')}))
    phone = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': _('Phone')}))
    email = forms.EmailField(label='', max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'email'}))
    text = forms.CharField(
        label='',
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'placeholder': _('Message Text'),
                'rows': '6',
            }
        ),
    )


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        data = form.cleaned_data
        subject = 'Сообщение от {name}'.format(**data)
        message = """
        Имя: {name}
        Телефон: {phone}
        Email: {email}
        Текст сообщения: {text}
        """.format(**data)
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
        return redirect('contact-success')


class ContactSuccessView(TemplateView):
    template_name = 'contact.html'


def test_error(request):
    raise Exception


def test_mail(request):
    send_mail('test', 'test', settings.DEFAULT_FROM_EMAIL, ['pavel@tyavin.name'])
    return HttpResponse('test email')


def robots_view(request):
    return HttpResponse('')


def humans_view(request):
    return HttpResponse('Tyavin Pavel')
