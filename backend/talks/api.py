from .models import Session
from .models import Slot
from rest_framework.viewsets import ModelViewSet


class SessionViewSet(ModelViewSet):
    model = Session


class SlotViewSet(ModelViewSet):
    model = Slot
