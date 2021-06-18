=====
Background changer
=====

The background changer is a Django app that changes the background to the uploaded image.

Quick start
-----------

1. Add "background_changer" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'background_changer',
    ]

2. Include the background_changer URLconf in your project urls.py like this::

    path('', include('background_changer.urls')),

3. Run ``python manage.py migrate`` to create the image model.

4. Visit http://127.0.0.1:8000/ to upload image and change background.
