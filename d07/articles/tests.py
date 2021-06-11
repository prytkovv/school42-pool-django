from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ArticleCreateViewTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        test_user = User.objects.create_user(**self.credentials)
        test_user.save()

    def test_redirect_if_not_logged_in(self):
        responce = self.client.get(reverse('articles:article_add'))
        self.assertRedirects(responce, '/accounts/login/?next=/articles/add/')

    def test_logged_in_uses_template(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('articles:article_add'))
        self.assertEqual(
            str(response.context['user']), self.credentials['username'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_add_form.html')


class PublicationListViewTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        test_user = User.objects.create_user(**self.credentials)
        test_user.save()

    def test_redirect_if_not_logged_int(self):
        response = self.client.get(reverse('articles:publications'))
        self.assertRedirects(response, '/accounts/login/?next=/publications/')

    def test_logged_in_uses_template(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('articles:publications'))
        self.assertEqual(
            str(response.context['user']), self.credentials['username'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/publication_list.html')


class UserFavoriteArticleListViewTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        test_user = User.objects.create_user(**self.credentials)
        test_user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('articles:favorites'))
        self.assertRedirects(response, '/accounts/login/?next=/favorites/')

    def test_logged_in_uses_template(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('articles:favorites'))
        self.assertEqual(
            str(response.context['user']), self.credentials['username'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/favorites.html')


class LoginViewTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        test_user = User.objects.create_user(**self.credentials)
        test_user.save()

    def test_login(self):
        response = self.client.post(
            '/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_redirect_if_logged_in(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('accounts:login'), follow=True)
        self.assertRedirects(response, reverse('articles:articles'))


class SignupViewTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        test_user = User.objects.create_user(**self.credentials)
        test_user.save()

    def test_redirect_if_logged_in(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('accounts:signup'), follow=True)
        self.assertRedirects(response, reverse('articles:articles'))
