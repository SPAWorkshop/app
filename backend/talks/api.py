from .models import Session
from .models import Talk
from rest_framework.viewsets import ModelViewSet


class SessionViewSet(ModelViewSet):
    model = Session


class TalkViewSet(ModelViewSet):
    model = Talk
