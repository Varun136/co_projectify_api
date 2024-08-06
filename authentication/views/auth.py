from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import (
    RegistrationUserSerializer, UserProfileSerializer,
    ResetPasswordSerializer
)
from authentication.models import UserAccount
from common.utils import (
    add_event_to_reset_password, get_user_obj, reset_password, 
    make_response, validate_confirmation_code, add_event_to_send_confirmation_code
)
from common.response import Errors, Responses


class RegisterUserView(CreateAPIView):
    """Register user"""

    serializer_class = RegistrationUserSerializer
    queryset = UserAccount.objects.all()
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user_id = response.data.get("id")
            user_email = response.data.get("email")
            add_event_to_send_confirmation_code(user_id, user_email)
            response.data = {
                "id": response.data.get("id")
            }
        return response


class ValidateConfirmationCode(APIView):
    """Validate the confirmation code for user signup"""

    def post(self, request, pk):
        code = request.data.get("code")
        if not validate_confirmation_code(pk, code):
            return make_response(
                Errors.INVALID_CODE.value,
                status.HTTP_400_BAD_REQUEST
            )
        user_obj = UserAccount.objects.get(id=pk)
        user_obj.is_active = True
        user_obj.save()
        return make_response({}, status.HTTP_200_OK)


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


