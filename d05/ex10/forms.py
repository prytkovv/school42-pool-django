from django import forms


from . import models


class SearchForm(forms.Form):

    movies_min_release_date = forms.DateField(
        label='Movie maximum release date')
    movies_max_release_date = forms.DateField(
        label='Movie minimum release date')
    planet_diameter = forms.IntegerField(
        label='Number greater than which the diameter of the planet should be')
    gender_selector = forms.ModelChoiceField(
        label='Choose gender to delete',
        queryset=models.Person.objects.values_list(
            'gender', flat=True).distinct(),)

