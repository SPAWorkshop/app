from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from rest_framework import routers
from talks.views import SessionViewSet
import accounts.urls


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'sessions', SessionViewSet)


urlpatterns = patterns('',
    url(r'^api/auth/', include(accounts.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/talks/(?P<pk>\d+)', 'talks.views.talk_detail', name='talk-detail'),
    url(r'^api/talks', 'talks.views.talk_list', name='talk-list'),
)
