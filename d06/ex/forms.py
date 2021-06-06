from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib import auth

from . import models


class LogInForm(forms.Form):

    username = forms.CharField(
        max_length=50,
        label='Username')
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(),
        label='Password')

    def clean(self):
        context = self.cleaned_data
        user = auth.authenticate(
            username=context.get('username'),
            password=context.get('password'))
        if not user or not user.is_active:
            raise forms.ValidationError('Incorrect username or password.')
        return context


class SignUpForm(forms.Form):

    username = forms.CharField(
        max_length=50,
        label='Username')
    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(),
        label='Password')
    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(),
        label='Repeat password')

    def clean_password2(self):
        context = self.cleaned_data
        password1 = context.get('password1')
        password2 = context.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords are not equal.')
        return password2

    def clean_username(self):
        cleaned_username = self.cleaned_data.get('username')
        if User.objects.filter(username=cleaned_username).exists():
            raise forms.ValidationError('Username is already taken.')
        return cleaned_username


class TipForm(ModelForm):

    class Meta:

        model = models.Tip
        fields = ['content']
        labels = {
            'content': 'Input tip text here',
        }
