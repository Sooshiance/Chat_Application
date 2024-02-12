from rest_framework import serializers

from .models import User, Profile


class RegisterUser(serializers.ModelSerializer):
    """
    Serializer class for Users
    """
    class Meta:
        model = User 
        fields = ['id', 'phone', 'email', 'first_name', 'last_name', 'bio', 'pic', 'role']


class UserProfile(serializers.ModelSerializer):
    """
    Serializer class for user's profile
    """
    class Meta:
        model = Profile 
        fields = ['user', 'phone', 'email', 'first_name', 'last_name', 'bio', 'pic', 'role']


class LoginSerializer(serializers.Serializer):
    """
    Serializer class for Login
    """
    phone = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': '••••••••••••'}
    )


class OTPSerializer(serializers.ModelSerializer):
    """
    Serializer class to recieve from Users
    """
    otp = serializers.CharField(required=True)
