from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied

from .models import Article, UserFavoriteArticle
from .forms import UserFavoriteArticleForm


def index(request):
    return redirect('articles:articles')


class ArticleListView(ListView):

    model = Article
    context_object_name = 'articles'
    queryset = Article.objects.order_by('created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headlines'] = (
            'Title', 'Synopsis', 'Author',
            'Created', 'When', '')
        return context


class ArticleDetailView(FormMixin, DetailView):

    model = Article
    form_class = UserFavoriteArticleForm
    context_object_name = 'article'

    def get_initial(self):
        return {'article': self.get_object(), 'user': self.request.user}

    def get_success_url(self):
        return reverse(
            'articles:article_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = Article
    fields = ('title', 'synopsis', 'content')
    template_name_suffix = '_add_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articles:publications')


class PublicationListView(LoginRequiredMixin, ListView):

    model = Article
    context_object_name = 'articles'
    template_name = 'articles/publication_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headlines'] = ('Title', 'Synopsis', 'Created', '')
        return context


class UserFavoriteArticleListView(LoginRequiredMixin, ListView):

    model = UserFavoriteArticle
    context_object_name = 'favorites'
    template_name = 'articles/favorites.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headlines'] = (
            'Title', 'Synopsis', 'Author', '')
        return context

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
