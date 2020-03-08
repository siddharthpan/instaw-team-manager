from rest_framework import serializers, exceptions, generics, permissions
from django.contrib.auth import authenticate
# from django.utils.six import text_type
from .models import CustomUser, UserGroups
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from team.settings import SIMPLE_JWT


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Subclassing the TokenObtainPairSerializer to add more claims
    in the payload section of the JWT
    """

    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        # print(user.password)

        # Adding Custom Claims
        token['username'] = user.username
        token['email'] = user.email

        # print(token)

        return token


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        data = {'access': str(refresh.access_token)}

        if SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
            if SIMPLE_JWT['BLACKLIST_AFTER_ROTATION']:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()

            data['refresh'] = str(refresh)

        return data


class RegistrationSerializer(serializers.ModelSerializer):
    "CustomUser serializer and creates a new User"

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)