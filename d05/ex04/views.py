from django.shortcuts import render
from django.http import HttpResponse


from . import forms


import psycopg2


dbconfig = {
    'host': 'localhost',
    'user': 'djangouser',
    'password': 'secret',
    'database': 'formationdjango'
}

def init(request):
    dbconnection = psycopg2.connect(**dbconfig)
    try:
        cursor = dbconnection.cursor()
        _SQL = """CREATE TABLE IF NOT EXISTS ex04_movies(
            title varchar(64) UNIQUE NOT NULL,
            episode_nb serial PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )"""
        cursor.execute(_SQL)
        dbconnection.commit()
        cursor.close()
    except psycopg2.Error as e:
        return HttpResponse(str(e))
    else:
        return HttpResponse('OK')
    finally:
        dbconnection.close()


def populate(request):
    movies = [
        {
            'title': "The Phantom Menace",
            'episode_nb': 1,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "Attack of the Clones",
            'episode_nb': 2,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-16"
        },
        {
            'title': "Revenge of the Sith",
            'episode_nb': 3,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-19"
        },
        {
            'title': "A New Hope",
            'episode_nb': 4,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "The Empire Strikes Back",
            'episode_nb': 5,
            'opening_crawl': "",
            'director': "Irvin Kershner",
            'producer': "Gary Kutz, Rick McCallum",
            'release_date': "1980-05-17"
        },
        {
            'title': "Return of the Jedi",
            'episode_nb': 6,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        },
        {
            'title': "The Force Awakens",
            'episode_nb': 7,
            'opening_crawl': "",
            'director': "J. J. Abrams",
            'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            'release_date': "2015-12-11"
        },
    ]
    dbconnection = psycopg2.connect(**dbconfig)
    try:
        cursor = dbconnection.cursor()
        result_list = [
            [movies[index]['title'], ]
            for index in range(len(movies))]
        item_counter = 0
        for movie in movies:
            _SQL = """INSERT INTO ex04_movies(
                title,
                episode_nb,
                director,
                producer,
                release_date) values (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (movie['title'],
                                  movie['episode_nb'],
                                  movie['director'],
                                  movie['producer'],
                                  movie['release_date'],))
            dbconnection.commit()
            result_list[item_counter].append('OK')
            item_counter += 1
    except psycopg2.Error as e:
        return HttpResponse(str(e))
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
            'ex04/populate.html',
            {'result_list': [i[1] for i in result_list]}
        )
    finally:
        dbconnection.close()


def display(request):
    dbconnection = psycopg2.connect(**dbconfig)
    try:
        cursor = dbconnection.cursor()
        _SQL = """SELECT * from ex04_movies"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        cursor.close()
    except psycopg2.Error as e:
        return HttpResponse(str(e))
    else:
        return render(request,
                      'ex04/display.html',
                      {'titles': ('Title',
                                  'Episode Number',
                                  'Opening crawl',
                                  'Director',
                                  'Producer',
                                  'Release date',),
                       'contents': contents})
    finally:
        dbconnection.close()


def remove(request):
    dbconnection = psycopg2.connect(**dbconfig)
    try:
        cursor = dbconnection.cursor()
        if request.method == 'POST':
            form = forms.MovieSelectionForm(request.POST)
            selected_movie_title = request.POST['titles']
            _SQL = """DELETE FROM ex04_movies WHERE title=%s"""
            cursor.execute(_SQL, (selected_movie_title, ))
            dbconnection.commit()
        _SQL = """SELECT title from ex04_movies"""
        cursor.execute(_SQL)
        movie_titles = [''.join(title) for title in cursor.fetchall()]
        cursor.close()
        form = forms.MovieSelectionForm(titles=movie_titles)
        if not movie_titles:
            return HttpResponse('No data available')
        return render(request,
                      'ex04/remove.html',
                      {'form': form})
    except psycopg2.Error as e:
        return HttpResponse(str(e))
    finally:
        dbconnection.close()
