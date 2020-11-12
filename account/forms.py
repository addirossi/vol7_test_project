from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm',
                  'email', 'first_name', 'last_name')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Имя пользователя уже занято')
        return username

    def clean(self):
        data = self.cleaned_data
        # data -> {'username': 'mark01', 'password': 'qwerty', 'password_confirm': 'qwerty', ...}
        password = data.get('password')
        password_confirm = data.pop('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        return user

#ChangePasswordForm(user=user)

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(required=True, widget=forms.PasswordInput)
    password = forms.CharField(min_length=6, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=6, required=True, widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Введён неверный пароль')
        return old_password

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return data
