from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, RegistrationSerializer
from .models import CustomUser, UserGroups, Permission, UserRoles, UserAuditLogs, ActivityLog, ActivityValue
from rest_framework import viewsets
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
import datetime
from itertools import groupby
from operator import itemgetter
from django.utils import timezone
import json
import requests
# from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth.tokens import default_token_generator
from django.urls.exceptions import NoReverseMatch
from django.utils.timezone import now
from datetime import date, timedelta
from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions, status, views, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from team.settings import PASSWORD_EXPIRY_DAYS

# Create your views here.

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = authenticate(username=request.data['email'], password=request.data['password'])
        if user is not None:
            print(user.is_active)
            if user.is_active:

                if timezone.now() - user.last_password_updated > timedelta(days=PASSWORD_EXPIRY_DAYS):
                    user.is_active = False
                    user.save()
                    return Response(
                        data={"message": "The password has expired,please generate a new one"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                else:

                    try:
                        user.login_failure_counts = 0
                        user.save()
                        serializer.is_valid(raise_exception=True)
                    except TokenError as e:
                        raise InvalidToken(e.args[0])

                    return Response(serializer.validated_data, status=status.HTTP_200_OK)
            else:
                return Response(
                    data={"message": "Your account is deactivated,contact the administrator"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            # Invalid login attempt
            # Getting the User
            user = CustomUser.objects.filter(email=request.data['email'])
            if user.exists():
                valid_user = CustomUser.objects.get(email=request.data['email'])
                valid_user.login_failure_counts = valid_user.login_failure_counts + 1
                valid_user.save()
                if valid_user.login_failure_counts == 3:
                    valid_user.is_active = False
                    valid_user.save()
                    return Response(
                        data={"message": "Your Account is Deactivated, after three failed login attempts"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                if not valid_user.is_active:
                    return Response(
                        data={"message": "Your account is deactivated,contact the administrator"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            return Response(
                data={
                    "message": "Invalid username or password(Account will be deactivated after three failed login attempts)"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CustomTokenRefreshView(TokenRefreshView):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    serializer_class = CustomTokenRefreshSerializer


class RegistrationAPIView(APIView):
    """
    API To Create Users
    """
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RegistrationSerializer

    def get(self, request):
        users = User.objects.users()

        user_resp = [{"username": user.username,
                      "email": user.email,
                      "firstname": user.firstname,
                      "lastname": user.lastname,
                      "date_Joined": user.date_joined.date(),
                      "is_active": user.is_active,

                      } for user in users]

        return Response(user_resp)

    def post(self, request):
        print("Inside reg")
        # Form Data
        user = json.loads(request.body)

        if CustomUser.objects.all().filter(email=user['email']).exists():
            return Response({"message": "User with the email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            CustomUser.objects.create_user(user)

            return Response(user, status=status.HTTP_201_CREATED)

