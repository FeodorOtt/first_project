from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.conf import settings
from django.utils import translation

from . import forms
from django.utils import translation


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
