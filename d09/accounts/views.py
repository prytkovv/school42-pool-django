from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import views as auth_views
from django.contrib import auth


def index(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/index.html')
    else:
        return redirect('accounts:signup')


class SignupView(CreateView):

    template_name = 'accounts/signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('accounts:login')


class LoginView(auth_views.LoginView):

    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('accounts:index')


def logout(request):
    auth.logout(request)
    return redirect('accounts:index')


def validate_username(request):
    username = request.GET.get('username', None)
    print(username)
    data = {
        'exists': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
