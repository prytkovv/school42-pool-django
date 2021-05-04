from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.AutoField(primary_key=True)
    open_crawl = models.TextField()
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateTimeField()

    def __str__(self):
        return self.title

