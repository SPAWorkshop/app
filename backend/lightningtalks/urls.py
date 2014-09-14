from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from rest_framework import routers
from talks.views import SessionViewSet
from talks.views import TalkViewSet
import accounts.urls


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'sessions', SessionViewSet)
router.register(r'talks', TalkViewSet)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include(accounts.urls)),
)
