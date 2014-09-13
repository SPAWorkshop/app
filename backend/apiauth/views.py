from . import models
from . import serializers
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import permissions


class RegistrationView(generics.CreateAPIView):
    http_method_names = ['post', 'options']
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserCreateSerializer

    #def post_save(self, obj, created):
        #auth_models.Token.objects.get_or_create(user=obj)

register = RegistrationView.as_view()


def activate(request):
    return JsonResponse({})


def login(request):
    return JsonResponse({})
