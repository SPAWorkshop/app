from django.db import models
from django.utils import timezone
from apiauth.models import User


class Session(models.Model):
    name = models.CharField(max_length=64, default='Lightning Talks')
    starts_at = models.DateTimeField()
    max_talks = models.PositiveSmallIntegerField(default=10)
    talk_time = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.name


class Talk(models.Model):
    session = models.ForeignKey(Session, related_name='talks')
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
