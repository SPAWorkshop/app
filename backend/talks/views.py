from .models import Session
from .models import Talk
from .serializers import SessionSerializer
from .serializers import TalkSerializer
from .serializers import TalkCreateSerializer
from .permissions import IsAdminOrReadOnly
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets


class SessionViewSet(viewsets.ModelViewSet):
    model = Session
    serializer_class = SessionSerializer
    permission_classes = [IsAdminOrReadOnly]


session_list = SessionViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


session_detail = SessionViewSet.as_view({
    'get': 'retrieve',
    'post': 'partial_update',
    'delete': 'destroy',
})


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


class TalkListViewSet(TalkViewSet):
    serializer_class = TalkCreateSerializer


talk_list = TalkListViewSet.as_view({
    'post': 'create',
    'get': 'list',
})


talk_detail = TalkViewSet.as_view({
    'get': 'retrieve',
    'post': 'partial_update',
    'delete': 'destroy',
})
