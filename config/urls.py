"""
URL configuration for config project.
"""


from django.contrib import admin
from django.urls import path, include

AUTH_BASE_URL = "api/auth/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(AUTH_BASE_URL, include('authentication.urls'))
]
