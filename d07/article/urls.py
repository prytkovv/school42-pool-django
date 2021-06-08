from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('articles/', views.ArticleListView.as_view(), name='article-list'),
    path('articles/add/', views.ArticleCreateView.as_view(), name='article-add'),
]
