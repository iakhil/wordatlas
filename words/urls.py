from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, GameOverView, RegisterView, BookmarkViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair_view'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', HomeView.as_view(), name='home'), 
    path('accounts/profile/game_over/', GameOverView.as_view(), name='game_over'), 
]