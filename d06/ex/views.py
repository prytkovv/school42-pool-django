from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import random

from . import forms


def init(request):
    if request.method == "POST":
        form = forms.TestForm(request.POST)
        text_field = request.POST['text_field']
        print(text_field)
        return HttpResponse(text_field)
    else:
        form = forms.TestForm()
    username = request.COOKIES.get('ex_username')
    if username is not None:
        response = render(request,
                          'ex/index.html',
                          {'username': username,
                           'form': form})
    else:
        username = random.choice(getattr(settings, 'USERNAMES', None))
        response = render(request,
                          'ex/index.html',
                          {'username': username,
                           'form': form})
        response.set_cookie(
            'ex_username',
            username,
            max_age=getattr(settings, 'SESSION_COOKIE_DURATION', None))
    return response
