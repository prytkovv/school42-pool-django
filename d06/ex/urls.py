from django.urls import path


from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:tip_id>/up/', views.upvote_tip, name='upvote'),
    path('<int:tip_id>/down', views.downvote_tip, name='downvote'),
    path('<int:tip_id>/delete', views.delete_tip, name='delete'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]
