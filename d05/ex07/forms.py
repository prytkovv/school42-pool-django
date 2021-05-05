from django import forms

from . import models


class SelectionMovieForm(forms.Form):
    movie_selector = forms.ModelChoiceField(
        label='Choose movie to delete:',
        queryset=models.Movie.objects.all())


class UpdateMovieForm(SelectionMovieForm):
    crawling_text = forms.CharField(
        label="Provide opening crawl to update",
        max_length=100)
