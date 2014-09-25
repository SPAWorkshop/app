from .models import Session
from .models import Talk
from rest_framework import serializers


class SessionListSerializer(serializers.ModelSerializer):
    talks_count = serializers.Field(source='talks.count')

    class Meta:
        model = Session
        fields = (
            'id',
            'name',
            'starts_at',
            'talk_time',
            'talks_count',
        )


# TODO: TASK I - SESSION DETAILS
# - create session retrieve serializer


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
        # TODO: TASK III - LIMIT TALKS
        # - implement validation
        pass


class TalkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talk
        fields = (
            'title',
        )

