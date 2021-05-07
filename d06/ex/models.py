from django.db import models


class Tip(models.Model):

    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)


