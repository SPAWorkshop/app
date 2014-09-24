from .models import Session
from .models import Talk
from .serializers import SessionSerializer
from .serializers import TalkSerializer
from .serializers import TalkCreateSerializer
from django.core.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets


class SessionList(generics.ListAPIView):
    model = Session
    serializer_class = SessionSerializer

session_list = SessionList.as_view()


class SessionDetail(generics.RetrieveAPIView):
    model = Session
    serializer_class = SessionSerializer

session_detail = SessionDetail.as_view()


class TalkViewSet(viewsets.ModelViewSet):
    model = Talk
    serializer_class = TalkSerializer

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def create(self, request):
        if not request.user.is_authenticated():
            raise PermissionDenied("Only authorized users may create talks")
        return super().create(request)


class TalkList(generics.ListCreateAPIView):
    model = Talk
    serializer_class = TalkCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def pre_save(self, obj):
        obj.author = self.request.user

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


talk_list = TalkList.as_view()


talk_detail = TalkViewSet.as_view({
    'get': 'retrieve',
    'post': 'partial_update',
    'delete': 'destroy',
})
