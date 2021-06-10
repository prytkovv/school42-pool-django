from django.forms import ModelForm
from django import forms

from .models import UserFavoriteArticle


class UserFavoriteArticleForm(ModelForm):

    class Meta:
        model = UserFavoriteArticle
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'article': forms.HiddenInput()}
