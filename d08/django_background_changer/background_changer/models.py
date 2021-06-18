from django.db import models


class Image(models.Model):

    title = models.CharField(max_length=150)
    upload = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
