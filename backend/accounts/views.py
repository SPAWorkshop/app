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


class ProfileView(generics.RetrieveAPIView):
    http_method_names = ['get', 'options']
    # default permission_classes are configured at settings
    serializer_class = serializers.UserCreateSerializer

    def get_object(self):
        if not self.request.user.is_authenticated():
            return None
        return self.request.user

profile = ProfileView.as_view()
