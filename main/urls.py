from django.urls import path
from .views import UserSkillsView

urlpatterns = [
    path("user-skill", UserSkillsView.as_view(), name="user-skill")
]