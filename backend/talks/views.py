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

session_list = SessionListView.as_view()


# TODO: TASK I - SESSION DETAILS
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
        # TODO: TASK II - CREATE TALK
        # - assign current user to newly created talk
        pass

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


talk_list = TalkListCreateView.as_view()


class TalkUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    model = Talk
    serializer_class = TalkUpdateSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        # TODO: TASK IV - UPDATE TALK
        # - create custom permission (allow modify talk only by author)
    )


talk_detail = TalkUpdateDestroyView.as_view()
