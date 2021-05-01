from django import forms


class TextMessageForm(forms.Form):
    text_message = forms.CharField(label='Text message', max_length=100)
