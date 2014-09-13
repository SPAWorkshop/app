from . import serializers
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authtoken import views as auth_views


class RegistrationView(generics.CreateAPIView):
    http_method_names = ['post', 'options']
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserCreateSerializer

register = RegistrationView.as_view()


class LoginView(auth_views.ObtainAuthToken):
    serializer_class = serializers.LoginUserSerializer


login = LoginView.as_view()
