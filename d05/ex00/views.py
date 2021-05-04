from django.http import HttpResponse

import psycopg2

dbconfig = {
    'host': 'localhost',
    'user': 'djangouser',
    'password': 'secret',
    'database': 'formationdjango',
}


def create_table():
    conn = psycopg2.connect(**dbconfig)
    try:
        cursor = conn.cursor()
        _SQL = """CREATE TABLE IF NOT EXISTS ex00_movies(
            title varchar(64) UNIQUE NOT NULL,
            episode_nb serial PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
        )"""
        cursor.execute(_SQL)
        conn.commit()
        cursor.close()
    except psycopg2.Error as e:
        return 'An error occured: %s' % str(e)
    finally:
        conn.close()
    return 'OK'


def init(request):
    return HttpResponse(create_table())
