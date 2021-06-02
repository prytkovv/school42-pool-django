from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import Http404


from . import forms
from . import models


class IndexView(ListView, ModelFormMixin):

    model = models.Tip
    template_name = 'ex/index.html'
    context_object_name = 'tips'
    form_class = forms.TipForm

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.author = self.request.user
            self.object.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        return context


@login_required
def upvote(request, tip_id):

    tip = get_object_or_404(models.Tip, pk=tip_id)
    tip.upvote(request.user)
    return redirect('index')


@login_required
def downvote(request, tip_id):

    tip = get_object_or_404(models.Tip, pk=tip_id)
    tip.downvote(request.user)
    return redirect('index')


class TipUpdateView(UpdateView):

    model = models.Tip
    fields = ['content']
    template_name_suffix = '_update_form'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author == request.user or request.user.is_staff:
            return super(
                TipUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

class TipDeleteView(DeleteView):

    model = models.Tip
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author == request.user or request.user.is_staff:
            return super(
                TipDeleteView, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

class LoginView(FormView):

    template_name = 'ex/login.html'
    form_class = forms.LoginForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(LoginView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        context = form.cleaned_data
        user = auth.authenticate(
            username=context.get('username'),
            password=context.get('password'))
        auth.login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


class SignupView(FormView):

    template_name = 'ex/signup.html'
    form_class = forms.SignupForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(SignupView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        context = form.cleaned_data
        user = User.objects.create_user(
            username=context.get('username'),
            password=context.get('password1'))
        user.save()
        auth.login(self.request, user)
        return super(SignupView, self).form_valid(form)

    def form_invalid(self, form):
        return super(SignupView, self).form_invalid(form)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')
