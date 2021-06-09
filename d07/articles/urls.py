from django.urls import path


from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticleListView.as_view(), name='article-list'),
    path('articles/add/', views.ArticleCreateView.as_view(), name='article-add'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('publications/', views.PublicationListView.as_view(), name='publication-list'),
    path('favorites/', views.UserFavoriteArticleListView.as_view(), name='favorite-list'),
]
