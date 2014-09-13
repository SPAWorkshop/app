from .models import Session
from rest_framework.serializers import ModelSerializer


class SessionSerializer(ModelSerializer):

    class Meta:
        model = Session
        fields = (
            'id',
            'name',
            'starts_at',
            'max_slots',
            'default_slot_time',
            'talks',
        )
        depth = 1