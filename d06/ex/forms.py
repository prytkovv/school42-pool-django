from django import forms
from django.forms import ModelForm
from . import models


class LoginForm(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(
        max_length=50, widget=forms.PasswordInput())


class SignupForm(LoginForm):

    confirmed_password = forms.CharField(
        max_length=50, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        confirmed_password = cleaned_data.get('confirmed_password')
        if password != confirmed_password:
            raise forms.ValidationError('Passwords are not equal')
        return cleaned_data


class TipForm(ModelForm):

    class Meta:

        model = models.Tip
        fields = ['content']
