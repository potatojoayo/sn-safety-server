from django.urls import path, include
from .views import LoginView, RegisterView, current_user, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView 



urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('',current_user,name='user'),
    path('logout/',LogoutView.as_view(),name='logout'), 
]

