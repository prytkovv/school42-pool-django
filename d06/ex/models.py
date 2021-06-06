from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import User


class Tip(models.Model):

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)

    def vote(self, voter, action):
        author = self.author.profile
        try:
            try:
                vote = Vote.objects.get(
                    voter=voter,
                    tip=self)
                if vote.action == action:
                    if vote.action == Vote.UP:
                        author.reputation -= 5
                    else:
                        author.reputation += 2
                    vote.delete()
                    return 'Vote canceled'
                return 'Already voted'
            except Vote.DoesNotExist:
                new_vote = Vote.objects.create(
                    voter=voter,
                    tip=self,
                    action=action)
                self.votes.add(new_vote)
                if new_vote.action == Vote.UP:
                    author.reputation += 5
                else:
                    author.reputation -= 2
                return 'Success'
            finally:
                author.save()
        except IntegrityError:
            return 'Unknown error'

    @property
    def score(self):
        return (self.votes.filter(
            action=Vote.UP).count() - self.votes.filter(
            action=Vote.DOWN).count())

    def __str__(self):
        return self.content

    class Meta:
        permissions = [('downvote', 'Can down vote')]


class Vote(models.Model):

    DOWN = 0
    UP = 1
    ACTIONS = (
        (DOWN, 'downvote'),
        (UP, 'upvote'),
    )

    voter = models.ForeignKey(
        User, on_delete=models.CASCADE)
    tip = models.ForeignKey(
        Tip, on_delete=models.CASCADE, related_name='votes')
    action = models.PositiveSmallIntegerField(
        blank=True, choices=ACTIONS)

    def __str__(self):
        return self.get_action_display()

    class Meta:
        unique_together = ('voter', 'tip')


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(default=0)
