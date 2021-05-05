from django import forms


class MovieSelectionForm(forms.Form):

    def __init__(self, titles, *args, **kwargs):
        super(MovieSelectionForm, self).__init__(*args, **kwargs)
        self.fields['titles'] = forms.ChoiceField(
            choices=[(title, title) for title in titles])

