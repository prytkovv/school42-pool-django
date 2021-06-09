from django.contrib import auth
from django.urls import reverse
from django.shortcuts import redirect


class LoginView(auth.views.LoginView):

    template_name = 'admin/login.html'
    extra_context = {
        'title': 'Login',
        'site_title': 'Articles',
        'site_header': 'Login'}

    def get_success_url(self):
        return reverse('articles:index')


def logout(request):
    auth.logout(request)
    return redirect('articles:index')
