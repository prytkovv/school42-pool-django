from django.shortcuts import render
from django.http import HttpResponse


from . import forms
from . import models


def populate(request):
    movies = [
        {
            'title': "The Phantom Menace",
            'episode_nb': 1,
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "Attack of the Clones",
            'episode_nb': 2,
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-16"
        },
        {
            'title': "Revenge of the Sith",
            'episode_nb': 3,
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-19"
        },
        {
            'title': "A New Hope",
            'episode_nb': 4,
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "The Empire Strikes Back",
            'episode_nb': 5,
            'director': "Irvin Kershner",
            'producer': "Gary Kutz, Rick McCallum",
            'release_date': "1980-05-17"
        },
        {
            'title': "Return of the Jedi",
            'episode_nb': 6,
            'director': "George Lucas",
            'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        },
        {
            'title': "The Force Awakens",
            'episode_nb': 7,
            'director': "J. J. Abrams",
            'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            'release_date': "2015-12-11"
        },
    ]
    result_list = [[movies[index]['title'], ] for index in range(len(movies))]
    item_counter = 0
    try:
        for m in movies:
            movie = models.Movie(title=m['title'],
                                 episode_nb=m['episode_nb'],
                                 director=m['director'],
                                 producer=m['producer'],
                                 release_date=m['release_date'])
            movie.save()
            result_list[item_counter].append('OK')
            item_counter += 1
    except KeyError as e:
        response = ''
        for i in result_list:
            if len(i) == 2:
                response += i[1] + '<br>'
            else:
                response += 'Key Error: %s in %s' % (e, i)
                break
        return HttpResponse(response)
    else:
        return render(
            request,
            'ex07/populate.html',
            {'result_list': [i[1] for i in result_list]}
        )


def display(request):
    return render(request,
                  'ex07/display.html',
                  {'titles': ('Title',
                              'Episode Number',
                              'Opening crawl',
                              'Director',
                              'Producer',
                              'Release date',
                              'Created',
                              'Updated'),
                   'movies': models.Movie.objects.all()})


def remove(request):
    if request.method == 'POST':
        form = forms.SelectionMovieForm(request.POST)
        if form.is_valid():
            selected_movie = request.POST['movie_selector']
            movie = models.Movie.objects.get(episode_nb=selected_movie)
            movie.delete()
    else:
        form = forms.SelectionMovieForm()
    if models.Movie.objects.all():
        return render(request,
                      'ex07/remove.html',
                      {'form': form})
    return HttpResponse('No data available')


def update(request):
    if request.method == 'POST':
        form = forms.UpdateMovieForm(request.POST)
        if form.is_valid():
            selected_movie = request.POST['movie_selector']
            crawling_text = request.POST['crawling_text']
            movie = models.Movie.objects.get(episode_nb=selected_movie)
            movie.opening_crawl = crawling_text
            movie.save()
    else:
        form = forms.UpdateMovieForm()
    if models.Movie.objects.all():
        return render(request,
                      'ex07/update.html',
                      {'form': form})
    return HttpResponse('No data available')
