from .models import Session
from .models import Talk
from .serializers import SessionSerializer
from .serializers import TalkSerializer
from .serializers import TalkCreateSerializer
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
