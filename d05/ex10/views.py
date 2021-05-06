from django.shortcuts import render
from django.http import HttpResponse


from . import forms
from . import models


def init(request):
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid:
            movies_max_release_date = request.POST['movies_max_release_date']
            movies_min_release_date = request.POST['movies_min_release_date']
            planet_diameter = request.POST['planet_diameter']
            selected_gender = request.POST['gender_selector']
            movies = models.Movie.objects.filter(release_date__range=[
                movies_min_release_date, movies_max_release_date]
            )
            result = []
            try:
                for movie in movies:
                    required_people = movie.characters.all().filter(
                        gender=selected_gender,
                        homeworld__diameter__gt=planet_diameter)
                    for person in required_people:
                        result_item = {
                            'movie_name': str(movie),
                            'person_name': str(person),
                            'gender': selected_gender,
                            'planet_name': str(person.homeworld),
                            'planet_diameter': str(person.homeworld.diameter)
                        }
                        result.append(result_item)
                return render(request,
                              'ex10/display.html',
                              {'titles': ('Movie',
                                          'Person',
                                          'Gender',
                                          'Planet',
                                          'Planet diameter',),
                               'result': result})
            except Exception as e:
                return HttpResponse(str(e))
    else:
        form = forms.SearchForm()
    return render(request, 'ex10/init.html', {'form': form})
