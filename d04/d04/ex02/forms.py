from django import forms


class TextMessageForm(forms.Form):
    text_message = forms.CharField(
        label='Please input something',
        max_length=100)
