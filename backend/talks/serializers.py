from .models import Session
from .models import Talk
from rest_framework.serializers import ModelSerializer


class SessionSerializer(ModelSerializer):

    class Meta:
        model = Session
        fields = (
            'id',
            'name',
            'starts_at',
            'max_talks',
            'talk_time',
            'talks',
        )
        depth = 1


class TalkSerializer(ModelSerializer):

    class Meta:
        model = Talk
        fields = (
            'id',
            'title',
            'author',
            'session',
        )
        read_only_fields = (
            'author',
        )