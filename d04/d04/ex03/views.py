from django.shortcuts import render


def index(request):
    return render(
        request,
        'ex03/index.html',
        {'rgb_list': list(range(0, 255, 5))})
