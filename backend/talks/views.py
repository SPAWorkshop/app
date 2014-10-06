from .models import Session
from .models import Talk
from .permissions import IsAuthor
from .serializers import SessionRetrieveSerializer
from .serializers import TalkListSerializer
from .serializers import TalkCreateSerializer
from .serializers import TalkUpdateSerializer
from .serializers import SessionListSerializer
from rest_framework import generics
from rest_framework import permissions


class SessionListView(generics.ListAPIView):
    model = Session
    serializer_class = SessionListSerializer


class SessionRetrieveView(generics.RetrieveAPIView):
    model = Session
    serializer_class = SessionRetrieveSerializer


class TalkListCreateView(generics.ListCreateAPIView):
    model = Talk
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TalkCreateSerializer
        return TalkListSerializer

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class TalkUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    model = Talk
    serializer_class = TalkUpdateSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsAuthor,
    )
