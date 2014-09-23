from accounts.models import User
from django.core.management.base import NoArgsCommand
from lightningtalks.utils import utc_datetime
from talks import models


def create_user(email, first_name, last_name, password):
    user = User.objects.create_user(email, first_name, last_name, password)
    print(' => Created user: {}'.format(user))
    return user


def create_session(name, starts_at):
    session = models.Session.objects.create(name=name, starts_at=starts_at)
    print(' => Creating session: {}'.format(session))
    return session


def create_talk(session, title, author):
    talk = models.Talk.objects.create(session=session, title=title, author=author)
    print(' => Create talk: {}'.format(talk))
    return talk


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        user = create_user('joe@doe.com', 'Joe', 'Doe', 'secret')
        first_session = create_session('Morning session', utc_datetime(2014, 9, 16, 9, 15))
        create_talk(first_session, 'JavaScript is broken', user)
        create_talk(first_session, 'Python is awesome', user)
        create_talk(first_session, 'AngularJS and Django', user)
        create_session('Evening session', utc_datetime(2014, 9, 15, 19, 30))
        create_session('Midnight session', utc_datetime(2014, 9, 22, 0, 0))
