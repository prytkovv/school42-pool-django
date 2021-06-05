from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import User


VOTE_ACTIONS = {
    'UP': 1,
    'DOWN': 0,
}


class Tip(models.Model):

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def upvote(self, voter):
        try:
            vote = Vote.objects.create(
                author=voter,
                tip=self,
                action=VOTE_ACTIONS['UP'])
            self.votes.add(vote)
            author_profile = self.author.profile
            author_profile.reputation += 5
            author_profile.save()
        except IntegrityError:
            vote = self.votes.get(
                author=voter,
                tip=self)
            vote.delete()
            return 'Voting canceled'
        else:
            return 'Succesfully voted'

    def downvote(self, voter):
        try:
            vote = Vote.objects.create(
                author=voter,
                tip=self,
                action=VOTE_ACTIONS['DOWN'])
            self.votes.add(vote)
            author_profile = self.author.profile
            author_profile.reputation -= 2
            author_profile.save()
        except IntegrityError:
            vote = self.votes.get(
                author=voter,
                tip=self)
            vote.delete()
            return 'Voting canceled'
        else:
            return 'Successfully voted'

    def get_rating(self):
        return (self.votes.filter(
            action=VOTE_ACTIONS['UP']).count() - self.votes.filter(
            action=VOTE_ACTIONS['DOWN']).count())

    def __str__(self):
        return self.content


class Vote(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    tip = models.ForeignKey(
        Tip, on_delete=models.CASCADE, related_name='votes')
    action = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        # change this
        return 'UP' if self.action else 'DOWN'

    class Meta:
        unique_together = ('author', 'tip',)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(default=0)
