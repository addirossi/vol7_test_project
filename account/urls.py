from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.urls import path

from .views import RegistrationView, SigninView

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('change_password/', PasswordChangeView.as_view(), name='change-password')
]