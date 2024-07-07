from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterUserView, UserProfileView, ForgotPasswordView, 
    ConfirmPasswordResetView
)

urlpatterns = [
    path("register", RegisterUserView.as_view(), name="user_register"),
    path("login", TokenObtainPairView.as_view(), name="user_login"),
    path("login/refresh", TokenRefreshView.as_view(), name="user_login_refresh"),
    path("user/<int:pk>/profile", UserProfileView.as_view(), name="user_profile"),
    path("reset-password", ForgotPasswordView.as_view(), name="reset-password"),
    path("confirm-password", ConfirmPasswordResetView.as_view(), name="confirm-password"),
]