from .models import Session
from .models import Talk
from .permissions import IsAuthor
from .serializers import SessionSerializer
from .serializers import TalkSerializer
from .serializers import TalkDetailSerializer
from rest_framework import generics
from rest_framework import permissions


class SessionList(generics.ListAPIView):
    model = Session
    serializer_class = SessionSerializer

session_list = SessionList.as_view()


class SessionDetail(generics.RetrieveAPIView):
    model = Session
    serializer_class = SessionSerializer

session_detail = SessionDetail.as_view()


class TalkList(generics.ListCreateAPIView):
    model = Talk
    serializer_class = TalkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


talk_list = TalkList.as_view()


class TalkDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Talk
    serializer_class = TalkDetailSerializer
    permission_classes = [IsAuthor]

    def update(self, *args, **kwargs):
        # partial update doesn't require all fields to be always present at
        # the request; so if we want to update only title, we only pass 'title'
        # and don't have to pass other fields that don't change (like 'author')
        kwargs['partial'] = True
        return super().update(*args, **kwargs)


talk_detail = TalkDetail.as_view()
