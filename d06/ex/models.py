from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import User


class Vote(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.ForeignKey('Tip', on_delete=models.CASCADE)
    choice = models.CharField(max_length=1, choices=[
        ('+', 'UPVOTE'),
        ('-', 'DOWNVOTE'),
    ])

    class Meta:
        unique_together = ('author', 'tip',)

    def reverse_choice(self):
        self.choice = '+' if self.choice == '-' else '-'
        self.save()

    def __str__(self):
        return self.choice


class Tip(models.Model):

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def get_rating(self):
        return self.vote_set.filter(
            choice='+').count() - self.vote_set.filter(choice='-').count()

    def upvote(self, voter):
        self_tip = self
        try:
            vote = Vote.objects.create(
                author=voter,
                tip=self_tip,
                choice='+')
            self_tip.vote_set.add(vote)
            self_tip.save()
        except IntegrityError:
            vote = self_tip.vote_set.get(author=voter)
            if str(vote) == '+':
                vote.delete()
            else:
                vote.reverse_choice()

    def downvote(self, voter):
        try:
            self_tip = self
            vote = Vote.objects.create(
                author=voter,
                tip=self_tip,
                choice='-')
            self_tip.vote_set.add(vote)
            self_tip.save()
        except IntegrityError:
            vote = self_tip.vote_set.get(author=voter)
            if str(vote) == '-':
                vote.delete()
            else:
                vote.reverse_choice()

    def __str__(self):
        return self.content
