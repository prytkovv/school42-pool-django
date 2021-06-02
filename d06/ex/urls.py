from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:tip_id>/up/', views.upvote, name='upvote'),
    path('<int:tip_id>/down/', views.downvote, name='downvote'),
    path('<int:pk>/edit/', login_required(
        views.TipUpdateView.as_view()), name='edit'),
    path('<int:pk>/delete/', login_required(
        views.TipDeleteView.as_view()), name='delete'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]
