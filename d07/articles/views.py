from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse


from .models import Article, UserFavoriteArticle


def index(request):
    return redirect('articles:article-list')


class ArticleListView(ListView):

    model = Article
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headlines'] = ('title', 'author', 'created', 'synopsis',)
        return context


class ArticleDetailView(DetailView):

    model = Article
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    fields = ('title', 'synopsis', 'content')
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articles:index')


class PublicationListView(LoginRequiredMixin, ListView):

    model = Article
    context_object_name = 'publications'
    template_name = 'articles/publication_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headlines'] = ('synopsis', 'created',)
        return context


class UserFavoriteArticleListView(LoginRequiredMixin, ListView):

    model = UserFavoriteArticle
    context_object_name = 'favorites'
    template_name = 'articles/favorites.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
