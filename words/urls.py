from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('game_over/', views.game_over, name='game_over'),
]