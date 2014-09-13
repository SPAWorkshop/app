from .models import Session
from .models import Talk
from .serializers import SessionSerializer
from .serializers import TalkSerializer
from rest_framework.viewsets import ModelViewSet


class SessionViewSet(ModelViewSet):
    model = Session
    serializer_class = SessionSerializer


class TalkViewSet(ModelViewSet):
    model = Talk
    serializer_class = TalkSerializer

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
