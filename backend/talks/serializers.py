from .models import Session
from .models import Talk
from accounts.models import User
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class TalkSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Talk
        fields = ['id', 'title', 'author', 'session']
        read_only_fields = ['id']

    def validate_session(self, attrs, field_name):
        session = attrs[field_name]
        if session.talks.count() >= session.max_talks:
            msg = 'Cannot add more talks to this session.'
            raise serializers.ValidationError(msg)
        return attrs

    def transform_session(self, obj, value):
        # this makes serializer return dictionary when *returning* object,
        # while preserves possibility to pass simple session.id when performing
        # create/update
        return {
            'id': obj.session_id,
            'name': obj.session.name,
        }


class TalkDetailSerializer(TalkSerializer):
    class Meta(TalkSerializer.Meta):
        read_only_fields = ['id', 'session']


class SessionSerializer(serializers.ModelSerializer):
    talks = TalkSerializer(many=True)

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
