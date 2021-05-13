from django.db import models
from django.contrib.auth.models import User


class Vote(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.ForeignKey('Tip', on_delete=models.CASCADE)
    choice = models.CharField(max_length=2)

    class Meta:
        unique_together = ('author', 'tip',)

    def reverse_choice(self):
        if self.choice == 'UP':
            self.choice = 'DN'
        elif self.choice == 'DN':
            print('here')
            self.choice = 'UP'
        self.save()

    def __str__(self):
        return self.choice


class Tip(models.Model):

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def get_tip_rating(self):
        return self.vote_set.filter(
            choice='UP').count() - self.vote_set.filter(choice='DN').count()

    def upvote(self, voter):
        my_tip = self
        vote = Vote.objects.create(
            author=voter,
            tip=my_tip,
            choice='UP')
        my_tip.vote_set.add(vote)
        my_tip.save()

    def downvote(self, voter):
        my_tip = self
        vote = Vote.objects.create(
            author=voter,
            tip=my_tip,
            choice='DN')
        my_tip.vote_set.add(vote)
        my_tip.save()

    def __str__(self):
        return self.content
