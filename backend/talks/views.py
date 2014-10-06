from .models import Session
from .models import Talk
from .serializers import TalkListSerializer
from .serializers import TalkCreateSerializer
from .serializers import TalkUpdateSerializer
from .serializers import SessionListSerializer
from rest_framework import generics
from rest_framework import permissions


class SessionListView(generics.ListAPIView):
    model = Session
    serializer_class = SessionListSerializer



# TODO: TASK 1 - SESSION DETAILS
# - create view (generics.RetrieveAPIView)


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
        # TODO: TASK 2 - CREATE TALK
        # - assign current user to newly created talk
        pass

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class TalkUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    model = Talk
    serializer_class = TalkUpdateSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        # TODO: TASK 4 - UPDATE TALK
        # - create custom permission (allow modify talk only by author)
    )
