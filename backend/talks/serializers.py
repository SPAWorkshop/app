from .models import Session
from .models import Talk
from rest_framework import serializers


class SessionSerializer(serializers.ModelSerializer):

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
        read_only_fields = (
            'talks',
        )
        depth = 1


class TalkSerializer(serializers.ModelSerializer):

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
            'session',
        )


class TalkCreateSerializer(TalkSerializer):

    class Meta(TalkSerializer.Meta):
        read_only_fields = ['author']

    def validate_session(self, attrs, field_name):
        session = attrs[field_name]
        if session.talks.count() >= session.max_talks:
            msg = 'Cannot add more talks to this session'
            raise serializers.ValidationError(msg)
        return attrs
