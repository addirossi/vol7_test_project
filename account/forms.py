from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm',
                  'first_name', 'last_name')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Имя пользователя уже занято')
        return username

    def clean(self):
        data = self.cleaned_data
        # data -> {'username': 'mark01', 'password': 'qwerty', 'password_confirm': 'qwerty', ...}
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        return user

# class UserManager:
#     def create_user(self, username, password, **kwargs):
#         ...
#
# User.objects.create_user(**self.cleaned_data)
# User.objects.create_user(username=username, password=password, first_name=first_name)