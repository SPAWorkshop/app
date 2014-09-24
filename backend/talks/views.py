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

session_list = SessionListView.as_view()


class SessionRetrieveView(generics.RetrieveAPIView):
    model = Session
    serializer_class = SessionRetrieveSerializer

session_detail = SessionRetrieveView.as_view()


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


talk_list = TalkListCreateView.as_view()


class TalkUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    model = Talk
    serializer_class = TalkUpdateSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsAuthor,
    )


talk_detail = TalkUpdateDestroyView.as_view()
