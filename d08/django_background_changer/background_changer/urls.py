from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'background_changer'
urlpatterns = [
    path('', views.ImageUploadView.as_view(), name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
