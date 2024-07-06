from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationUserSerializer


class RegisterUserView(CreateAPIView):
    """Register user"""
    serializer_class = RegistrationUserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            response.data = {
                "id": response.data.get("id")
            }
        return response



