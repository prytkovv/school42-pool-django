from django.forms import ModelForm

from .models import UserFavoriteArticle


class UserFavoriteArticleForm(ModelForm):

    class Meta:
        model = UserFavoriteArticle
        fields = []
