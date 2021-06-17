from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views import View
from django.urls import reverse

from .models import Image


class ImageUploadView(CreateView):

    model = Image
    fields = ['title', 'upload']
    template_name_suffix = '_upload_form'

    def get_object(self):
        return self.model.objects.last()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['background_image'] = self.get_object()
        return context

    def get_success_url(self):
        return reverse('background_changer:upload')

    def form_valid(self, form):
        return super().form_valid(form)

