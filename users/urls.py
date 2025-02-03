# users/urls.py
from django.urls import path
from .views import RegisterView, LoginView, EditUserView, RequestPasswordResetView, ResetPasswordView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('edit-user/', EditUserView.as_view(), name='edit-user'),
    path('request-password-reset/', RequestPasswordResetView.as_view(), name='request-password-reset'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
]
