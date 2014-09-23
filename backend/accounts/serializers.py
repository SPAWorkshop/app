from . import constants
from . import models
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['email', 'password', 'first_name', 'last_name']
        write_only_fields = ['password']

    def restore_object(self, attrs, instance=None):
        user = models.User(
            email=attrs['email'],
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
        )
        user.set_password(attrs['password'])
        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError(constants.INACTIVE_ACCOUNT_ERROR)
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError(constants.INVALID_CREDENTIALS_ERROR)
        else:
            raise serializers.ValidationError(constants.MISSING_DATA_ERROR)
