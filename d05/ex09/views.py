from django.shortcuts import render


from . import models


def display(request):
    return render(request,
                  'ex09/display.html',
                  {'titles': ('Name', 'Homeworld', 'climate'),
                   'peoples': models.Person.objects.filter(
                      homeworld__climate__contains='windy').order_by('name')})

