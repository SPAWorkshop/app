from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^activate$', views.activate, name='activate'),
    url(r'^login$', views.login, name='login'),
]
