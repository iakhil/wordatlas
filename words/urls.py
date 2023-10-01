from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, GameOverView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'), 
    path('game_over/', GameOverView.as_view(), name='game_over'), 
]