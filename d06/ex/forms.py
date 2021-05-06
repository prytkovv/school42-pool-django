from django import forms


class TestForm(forms.Form):

    text_field = forms.CharField(max_length=100)
