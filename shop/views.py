from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.utils.timezone import now, make_naive
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from shop.models import HomeImage, Category


class StubView(TemplateView):
    template_name = 'stub.html'


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['home_image_list'] = HomeImage.objects.all()
        n = make_naive(now())
        weekday_dict = {
            0: 'понедельник',
            1: 'вторник',
            2: 'среда',
            3: 'четверг',
            4: 'пятница',
            5: 'суббота',
            6: 'воскресенье',
        }

        ctx['weekday'] = weekday_dict[n.weekday()]
        ctx['open_text'] = 'Мы открыты !' if 12 <= n.hour < 22 else 'Мы закрыты.'
        return ctx


class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category_list'] = Category.objects.all()
        return ctx


class ShippingView(TemplateView):
    template_name = 'shipping.html'


class VacancyView(TemplateView):
    template_name = 'shipping.html'


class NewsView(TemplateView):
    template_name = 'shipping.html'


class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    phone = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    email = forms.EmailField(label='', max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'email'}))
    text = forms.CharField(
        label='',
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Текст сообщения',
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

