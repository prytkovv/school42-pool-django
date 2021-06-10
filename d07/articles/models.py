from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    synopsis = models.CharField(max_length=312)
    content = models.TextField()

    def __str__(self):
        return self.title


class UserFavoriteArticle(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='favorite')

    class Meta:
        unique_together = ('user', 'article')

    def __str__(self):
        return self.article.title
