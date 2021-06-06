from django.shortcuts import redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .forms import TipForm, LogInForm, SignUpForm
from .models import Tip, Vote


class IndexView(ListView, ModelFormMixin):

    model = Tip
    template_name = 'ex/index.html'
    context_object_name = 'tips'
    form_class = TipForm

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

        return redirect('index')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        return context


@login_required
def upvote(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    messages.info(request, tip.vote(request.user, Vote.UP))
    return redirect('index')


@login_required
@user_passes_test(
    lambda user: user.profile.reputation >= 15)
def downvote(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    messages.info(request, tip.vote(request.user, Vote.DOWN))
    return redirect('index')


class TipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Tip
    fields = ['content']
    template_name_suffix = '_update_form'
    success_url = '/'

    def test_func(self):
        return (self.request.user.profile.reputation >= 30
            or self.request.user == self.get_object().author)


class TipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Tip
    success_url = '/'

    def test_func(self):
        return (self.request.user.profile.reputation >= 30
            or self.request.user == self.get_object().author)


class LogInView(FormView):

    template_name = 'ex/login.html'
    form_class = LogInForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(LogInView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LogInView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        context = form.cleaned_data
        user = auth.authenticate(
            username=context.get('username'),
            password=context.get('password'))
        auth.login(self.request, user)
        return super(LogInView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LogInView, self).form_invalid(form)


class SignUpView(FormView):

    template_name = 'ex/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(SignUpView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        context = form.cleaned_data
        user = User.objects.create_user(
            username=context.get('username'),
            password=context.get('password1'))
        user.save()
        auth.login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def form_invalid(self, form):
        return super(SignUpView, self).form_invalid(form)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')
