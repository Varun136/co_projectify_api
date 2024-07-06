from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationUserSerializer(serializers.ModelSerializer):
    """Serializer for validating user sign-up data"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        print(user.password)
        return user