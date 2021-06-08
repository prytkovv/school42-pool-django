from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import auth
from django.urls import reverse


from .models import Article


def index(request):
    return redirect('article-list')


class LoginView(auth.views.LoginView):

    template_name = 'admin/login.html'
    extra_context = {
        'title': 'Login',
        'site_title': 'Articles',
        'site_header': 'Login'}

    def get_success_url(self):
        return reverse('index')


class ArticleListView(ListView):

    model = Article
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headlines'] = ('title', 'author', 'created', 'synopsis',)
        return context


class PublicationListView(LoginRequiredMixin, ListView):

    model = Article
    context_object_name = 'publications'
    template_name = 'article/publication_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headlines'] = ('synopsis', 'created',)
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    fields = ('title', 'synopsis', 'content')
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


def logout(request):
    auth.logout(request)
    return redirect('index')
