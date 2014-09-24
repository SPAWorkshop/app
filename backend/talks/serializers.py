from .models import Session
from .models import Talk
from accounts.models import User
from rest_framework import serializers


class SessionListSerializer(serializers.ModelSerializer):
    talks_count = serializers.Field(source='talks.count')

    class Meta:
        model = Session
        fields = (
            'id',
            'name',
            'starts_at',
            'max_talks',
            'talk_time',
            'talks_count',
        )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
        )


class SessionTalkSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Talk
        fields = (
            'id',
            'title',
            'author',
        )


class SessionRetrieveSerializer(serializers.ModelSerializer):
    talks = SessionTalkSerializer(many=True)

    class Meta:
        model = Session
        fields = (
            'name',
            'starts_at',
            'max_talks',
            'talk_time',
            'talks',
        )


class TalkSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = (
            'id',
            'name',
        )


class TalkListSerializer(serializers.ModelSerializer):
    session = TalkSessionSerializer()

    class Meta:
        model = Talk
        fields = (
            'id',
            'title',
            'author',
            'session',
        )


class TalkCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talk
        fields = (
            'title',
            'session',
        )

    def validate_session(self, attrs, field_name):
        session = attrs[field_name]
        if session.talks.count() >= session.max_talks:
            msg = 'Cannot add more talks to this session.'
            raise serializers.ValidationError(msg)
        return attrs


class TalkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talk
        fields = (
            'title',
        )

