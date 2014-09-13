from django.db import models
from django.utils import timezone


class Session(models.Model):
    name = models.CharField(max_length=64, default='Lightning Talks')
    starts_at = models.DateTimeField()
    max_slots = models.PositiveSmallIntegerField(default=10)
    default_slot_time = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.name


class Talk(models.Model):
    session = models.ForeignKey(Session, related_name='talks')
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('session', 'number')

    def __str__(self):
        return self.title
