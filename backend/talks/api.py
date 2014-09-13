from .models import Session
from .models import Talk
from .serializers import SessionSerializer
from rest_framework.viewsets import ModelViewSet


class SessionViewSet(ModelViewSet):
    model = Session
    serializer_class = SessionSerializer


class TalkViewSet(ModelViewSet):
    model = Talk
