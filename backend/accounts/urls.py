from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^me$', views.profile, name='profile'),
    # TODO:
    # - /logout
    # - /activate
    # - /password-reset
    # - /password-reset-confirm
    # - /password-change
]
