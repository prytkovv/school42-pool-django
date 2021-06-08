from django.views.generic.list import ListView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import auth


from .models import Article
from .forms import LoginForm


def index(request):
    return redirect('article-list')


class ArticleListView(ListView):

    model = Article
    context_object_name = 'articles'

    def get_context_data(self, *args, **kwargs):
        context = super(
            ArticleListView, self).get_context_data(*args, **kwargs)
        context['headlines'] = ('title', 'author', 'created', 'synopsis',)
        return context


class LoginView(FormView):

    form_class = LoginForm
    success_url = '/'
    template_name = 'article/login.html'

    def form_valid(self, form):
        context = form.cleaned_data
        user = auth.authenticate(
            username=context.get('username'),
            password=context.get('password'))
        auth.login(self.request, user)
        return super().form_valid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):

    login_url = '/login/'
    model = Article
    fields = ('title', 'synopsis', 'content')
    template_name_suffix = '_create_form'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def logout(request):
    auth.logout(request)
    return redirect('index')
