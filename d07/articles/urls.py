from django.urls import path

from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles/add/', views.ArticleCreateView.as_view(), name='article_add'),
    path('articles/<int:pk>/', views.ArticleView.as_view(), name='article_detail'),
    path('publications/', views.PublicationListView.as_view(), name='publications'),
    path('favorites/', views.UserFavoriteArticleListView.as_view(), name='favorites'),
]
