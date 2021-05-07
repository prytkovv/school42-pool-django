from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db import IntegrityError

from . import forms
from . import models


def index(request):
    tips = models.Tip.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.author = str(request.user)
                tip.save()
        else:
            form = forms.TipForm()
        return render(request,
                      'ex/index.html',
                      {'tips': tips,
                       'username': request.user,
                       'form': form})
    else:
        return render(request,
                      'ex/index.html',
                      {'username': request.user})


def login(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method == 'POST':
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = auth.authenticate(
                    username=data.get('username'),
                    password=data.get('password'))
                if user:
                    if user.is_active:
                        auth.login(request, user)
                        return redirect(index)
                else:
                    messages.error(request,
                                   'Username or password is not correct')
                    return render(request,
                                  'ex/login.html',
                                  {'form': form,
                                   'form.username': data.get('username'),
                                   'username': request.user})
        else:
            form = forms.LoginForm()
    return render(request,
                  'ex/login.html',
                  {'form': form,
                   'username': request.user})


def signup(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method == 'POST':
            form = forms.SignupForm(request.POST)
            if form.is_valid():
                try:
                    user = User.objects.create_user(
                        username=form.cleaned_data.get('username'),
                        password=form.cleaned_data.get('password'))
                    user.save()
                    auth.login(request, user)
                except IntegrityError:
                    messages.error(request, 'Username is not available')
                return redirect(index)
        else:
            form = forms.SignupForm()
    return render(request,
                  'ex/signup.html',
                  {'form': form,
                   'username': request.user})


def logout(request):
    auth.logout(request)
    return redirect(index)
