from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationUserSerializer, UserProfileSerializer
from .models import UserAccount


class RegisterUserView(CreateAPIView):
    """Register user"""
    serializer_class = RegistrationUserSerializer
    queryset = UserAccount.objects.all()

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            response.data = {
                "id": response.data.get("id")
            }
        return response
    
class UserProfileView(RetrieveAPIView):
    """User profile"""
    queryset = UserAccount.objects.all()
    serializer_class = UserProfileSerializer



