from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('index-page')


class SigninView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index-page')

#TODO: Смена пароля


#TODO: Забыли пароль
#TODO: Сверстать страницы на BootStrap
#TODO: Залить на сервер

