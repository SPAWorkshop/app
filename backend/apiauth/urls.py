from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register$', views.register),
    url(r'^activate$', views.activate),
    url(r'^login$', views.login),
]
