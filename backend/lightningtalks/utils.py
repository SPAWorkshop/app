from django.utils import timezone
import datetime


def utc_datetime(*args):
    dt = datetime.datetime(*args)
    return timezone.make_aware(dt, timezone.utc)
