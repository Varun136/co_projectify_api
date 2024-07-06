from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView

urlpatterns = [
    path("register", RegisterUserView.as_view(), name="user_register"),
    path("login", TokenObtainPairView.as_view(), name="user_login"),
    path("login/refresh", TokenRefreshView.as_view(), name="user_login_refresh")

]