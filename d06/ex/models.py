from django.db import models
from django.contrib.auth.models import User

class Tip(models.Model):

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    user_upvotes = models.ManyToManyField(
        User, blank=True, related_name='tip_upvotes')
    user_downvotes = models.ManyToManyField(
        User, blank=True, related_name='tip_downvotes')

    def get_rating(self):
        return self.user_upvotes.count() - self.user_downvotes.count()

    def __str__(self):
        return self.content
