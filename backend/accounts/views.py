from . import serializers
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authtoken import views as auth_views


class RegistrationView(generics.CreateAPIView):
    http_method_names = ['post', 'options']
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserCreateSerializer


class LoginView(auth_views.ObtainAuthToken):
    serializer_class = serializers.LoginUserSerializer



class ProfileView(generics.RetrieveAPIView):
    http_method_names = ['get', 'options']
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserCreateSerializer

    def get_object(self):
        return self.request.user
