from django.urls import path


from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:tip_id>/up/', views.upvote, name='upvote'),
    path('<int:tip_id>/down/', views.downvote, name='downvote'),
    path('<int:pk>/edit/', views.TipUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TipDeleteView.as_view(), name='delete'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]
