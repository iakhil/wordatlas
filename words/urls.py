from django.urls import path
from .views import HomeView, GameOverView

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('game_over/', GameOverView.as_view(), name='game_over'), 
]