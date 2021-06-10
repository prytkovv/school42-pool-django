from django.contrib import auth
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class SignupView(CreateView):

    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return reverse('articles:index')


class LoginView(auth.views.LoginView):

    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('articles:index')


def logout(request):
    auth.logout(request)
    return redirect('articles:index')
