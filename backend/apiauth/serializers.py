from . import constants
from . import models
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['email', 'password']
        write_only_fields = ['password']  # use another enpoint to change pwd

    def restore_object(self, attrs, instance=None):
        user = models.User(email=attrs['email'])
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
                    raise serializers.ValidationError(constants.DISABLE_ACCOUNT_ERROR)
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError(constants.INVALID_CREDENTIALS_ERROR)
        else:
            raise serializers.ValidationError(constants.MISSING_DATA_ERROR)
