from accounts.models import User
from django.core.management.base import NoArgsCommand
from django.utils import timezone
from talks import models
import datetime


def utc_datetime(*args):
    dt = datetime.datetime(*args)
    return timezone.make_aware(dt, timezone.utc)


def create_user(email, password):
    user = User.objects.create_user(email, password)
    print(" => Created user: %s" % user)
    return user


def create_session(name, starts_at):
    session = models.Session.objects.create(name=name, starts_at=starts_at)
    print(" => Creating session: %s" % session)
    return session


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        create_user('joe@doe.com', 'secret')

        create_session('Evening session', utc_datetime(2014, 9, 15, 19))
        create_session('Morning talks', utc_datetime(2014, 9, 16, 12))
        create_session('PyWaw #40', utc_datetime(2014, 9, 22, 18, 30))
