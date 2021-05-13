from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.db import IntegrityError
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.views.generic.edit import ModelFormMixin


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
        context['username'] = self.request.user
        return context


def upvote_tip(request, tip_id):

    try:
        tip = models.Tip.objects.get(pk=tip_id)
        user = request.user
        tip.upvote(user)
    except IntegrityError:
        tip_vote = tip.vote_set.get(author=user)
        if str(tip_vote) == 'UP':
            tip_vote.delete()
        else:
            tip_vote.reverse_choice()
    finally:
        return redirect('index')


def downvote_tip(request, tip_id):

    try:
        tip = models.Tip.objects.get(pk=tip_id)
        user = request.user
        tip.downvote(user)
    except IntegrityError:
        tip_vote = tip.vote_set.get(author=user)
        if str(tip_vote) == 'DN':
            tip_vote.delete()
        else:
            tip_vote.reverse_choice()
    finally:
        return redirect('index')


def delete_tip(request, tip_id):

    tip = models.Tip.objects.get(pk=tip_id)
    tip.delete()
    return redirect('index')


class LoginView(FormView):

    template_name = 'ex/login.html'
    form_class = forms.LoginForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['username'] = self.request.user
        return context

    def form_valid(self, form):
        context = form.cleaned_data
        user = auth.authenticate(
            username=context.get('username'),
            password=context.get('password'))
        if user:
            if user.is_active:
                auth.login(self.request, user)
                return redirect('index')
        else:
            messages.error(self.request,
                           'Username or password is not correct')
            return super(LoginView, self).form_valid(form)


class SignupView(FormView):

    template_name = 'ex/signup.html'
    form_class = forms.SignupForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        context['username'] = self.request.user
        return context

    def form_valid(self, form):
        context = form.cleaned_data
        try:
            user = User.objects.create_user(
                username=context.get('username'),
                password=context.get('password'))
            user.save()
            auth.login(self.request, user)
        except IntegrityError:
            messages.error(self.request, 'Username is not available')
            return super(SignupView, self).form_valid(form)
        else:
            return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')
