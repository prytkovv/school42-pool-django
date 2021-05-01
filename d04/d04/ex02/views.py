from django.shortcuts import render


from . import forms


def get_text_message(request):
    if request.method == 'POST':
        form = forms.TextMessageForm(request.POST)
        if form.is_valid():
            return render(
                request,
                'ex02/text_message.html',
                {'text_message': form.cleaned_data['text_message']}
            )
    else:
        form = forms.TextMessageForm()
    return render(request, 'ex02/form.html', {'form': form})
