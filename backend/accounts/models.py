from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, **kwargs):
        user = self.model(email=email,
                          first_name=first_name,
                          last_name=last_name,
                          **kwargs)
        user.set_password(password)
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    """
    Similar to base Django user however main natural ID field is ``email``,
    not the ``username`` (which is not even included).
    """
    email = models.EmailField(unique=True, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    is_staff = models.BooleanField(default=False, db_index=True)
    first_logged_at = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    # required by django-registration
    @property
    def username(self):
        return self.email
