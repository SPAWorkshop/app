from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers
from talks.api import SessionViewSet
from talks.api import TalkViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'sessions', SessionViewSet)
router.register(r'talks', TalkViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
