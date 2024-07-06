from rest_framework import serializers
from .models import UserAccount

class RegistrationUserSerializer(serializers.ModelSerializer):
    """Serializer for validating user sign-up data"""
    
    class Meta:
        model = UserAccount
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 
            'password', 'age', 'gender'
        ]
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = UserAccount.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for giving the short profile information about user"""

    class Meta:
        model = UserAccount
        fields = [
            'id', 'full_name', 'username', 'email'
        ]