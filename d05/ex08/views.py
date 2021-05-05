from django.shortcuts import render
from django.http import HttpResponse


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
        _SQL = """
            CREATE TABLE IF NOT EXISTS ex08_planets(
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) NOT NULL UNIQUE,
                climate TEXT,
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            );
            CREATE TABLE IF NOT EXISTS ex08_people(
                id SERIAL PRIMARY KEY,
                name VARCHAR(64),
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64),
                FOREIGN KEY(homeworld)
                REFERENCES ex08_planets(name)
            );
        """
        cursor.execute(_SQL)
        cursor.close()
        dbconnection.commit()
    except psycopg2.Error as e:
        return HttpResponse(str(e))
    finally:
        dbconnection.close()
    return HttpResponse('OK')


def populate(request):
    dbconnection = psycopg2.connect(**dbconfig)
    populate_result = ''
    try:
        cursor = dbconnection.cursor()
        with open('resources/planets.csv') as f:
            cursor.copy_from(f, 'ex08_planets', columns=(
                'name', 'climate', 'diameter', 'orbital_period',
                'population', 'rotation_period', 'surface_water', 'terrain'),
                null='NULL')
        populate_result += 'OK<br>'
        with open('resources/people.csv') as f:
            cursor.copy_from(f, 'ex08_people', columns=(
                'name', 'birth_year', 'gender', 'eye_color',
                'hair_color', 'height', 'mass', 'homeworld'),
                null='NULL')
        populate_result *= 2
        cursor.close()
        dbconnection.commit()
        return HttpResponse(populate_result)
    except Exception as e:
        print(populate_result)
        return HttpResponse('%sError: %s' % (populate_result, (str(e)),))
    finally:
        dbconnection.close()


def display(request):
    dbconnection = psycopg2.connect(**dbconfig)
    try:
        cursor = dbconnection.cursor()
        _SQL = """
            SELECT ex08_people.name,
                   ex08_people.homeworld,
                   ex08_planets.climate
            FROM ex08_people
            INNER JOIN ex08_planets
            ON ex08_people.homeworld = ex08_planets.name
            WHERE ex08_planets.climate LIKE '%windy%';
        """
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        print(contents)
        cursor.close()
        return render(request,
                      'ex08/display.html',
                      {'titles': ('Name', 'Homeworld', 'Climate',),
                       'contents': contents})
    except psycopg2.Error as e:
        return HttpResponse(str(e))
    finally:
        dbconnection.close()

