from django import forms

from . import models


class SelectionMovieForm(forms.Form):
    title_selector = forms.ModelChoiceField(
        label='Choose movie to delete:',
        queryset=models.Movie.objects.all())
