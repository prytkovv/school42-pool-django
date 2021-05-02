from django.shortcuts import render
from django.conf import settings

import datetime

from . import forms


def create_record(record):
    with open(getattr(settings, 'LOGFILE', None), 'a') as f:
        current_datetime = str(
            datetime.datetime.today().replace(
                microsecond=0)).split()
        f.write(
            'Message=%s;Date=%s;Time=%s\n'
            % (record, current_datetime[0], current_datetime[1])
        )


def get_record_list():
    try:
        with open(getattr(settings, 'LOGFILE', None)) as f:
            return [
                {
                    item.split('=')[0]: item.split('=')[1]
                    for item in record.split(';')
                }
                for record in f.readlines()
            ]
    except FileNotFoundError:
        return []


def get_text_message(request):
    if request.method == 'POST':
        form = forms.TextMessageForm(request.POST)
        if form.is_valid():
            text_message = form.cleaned_data['text_message']
            create_record(text_message)
    else:
        form = forms.TextMessageForm()
    return render(
        request, 'ex02/form.html',
        {'form': form, 'record_list': get_record_list()}
    )
