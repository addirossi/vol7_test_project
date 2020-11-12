from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from .forms import RegistrationForm, ChangePasswordForm


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('index-page')


class SigninView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index-page')


class PasswordChangeView(FormView):
    form_class = ChangePasswordForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('change-password-done')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PasswordChangeDoneView(TemplateView):
    template_name = 'account/change_password_done.html'

#TODO: Забыли пароль
#TODO: Сверстать страницы на BootStrap
#TODO: Залить на сервер

