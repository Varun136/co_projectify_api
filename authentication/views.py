from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    RegistrationUserSerializer, UserProfileSerializer,
    ResetPasswordSerializer
)
from .models import UserAccount
from common.utils import (
    add_event_to_reset_password, get_user_obj, reset_password, 
    make_response
)
from common.response import Errors, Responses


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


class ForgotPasswordView(APIView):
    """Handle forgot password"""
    
    def post(self, request):
        email_or_username = request.data.get("email_or_username")
        user_obj = get_user_obj(email_or_username)
        if not user_obj:
            return make_response(
                Errors.USER_NOT_FOUND.value, 
                status.HTTP_404_NOT_FOUND
            )

        add_event_to_reset_password(user_obj)
        return make_response(
            Responses.SEND_SUCCESS.value,
            status.HTTP_200_OK
        )


class ConfirmPasswordResetView(APIView):
    """Handle password reset"""

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reset, response = reset_password(serializer.data)
        if reset:
            return make_response(
                response,
                status.HTTP_200_OK
            )
        
        return make_response(
            response,
            status.HTTP_400_BAD_REQUEST
        )


