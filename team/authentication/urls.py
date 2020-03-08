from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.RegistrationAPIView.as_view()),
    path('token/obtain/', views.CustomTokenObtainPairView.as_view()),
    path('token/refresh/', views.CustomTokenRefreshView.as_view()),
    ]

