from accounts.models import User
from django.core.urlresolvers import reverse
from lightningtalks.utils import utc_datetime
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from talks.models import Session
from talks.models import Talk


class TestTalk(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('joe@doe.com', 'Joe', 'Doe', 'pwd')
        self.token = Token.objects.create(user=self.user)
        self.session = Session.objects.create(
            name='LH Session',
            starts_at=utc_datetime(2014, 10, 15, 19),
            max_talks=2,
        )
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create(self):
        response = self.client.post(reverse('talk-list'), {
            'session': self.session.id,
            'title': 'Joe Talk',
        })

        self.assertEqual(response.status_code, 201)

        talk = Talk.objects.get(title='Joe Talk')
        self.assertEqual(talk.author, self.user)

    def test_create_cannot_exceed_over_session_limit(self):
        Talk.objects.create(title='T1', author=self.user, session=self.session)
        Talk.objects.create(title='T2', author=self.user, session=self.session)

        response = self.client.post(reverse('talk-list'), {
            'session': self.session.id,
            'title': 'Joe Talk',
        })

        self.assertEqual(response.status_code, 400, response.data)
        self.assertIn('non_field_errors', response.data)

    def test_update(self):
        talk = Talk.objects.create(title='Joe Talk',
                                   author=self.user,
                                   session=self.session)

        url = reverse('talk-detail', kwargs={'pk': talk.id})
        response = self.client.post(url, {
            'title': 'TDD',
        })

        self.assertEqual(response.status_code, 200, response.data)

        fetched = Talk.objects.get(id=talk.id)
        self.assertEqual(fetched.title, 'TDD')

    def test_update_session_should_not_be_changed(self):
        talk = Talk.objects.create(title='Joe Talk',
                                   author=self.user,
                                   session=self.session)

        start = utc_datetime(2014, 10, 21, 14)
        session2 = Session.objects.create(name='StormTalks', starts_at=start)

        url = reverse('talk-detail', kwargs={'pk': talk.id})
        response = self.client.post(url, {
            'title': 'TDD',
            'session': session2.pk,

        })

        self.assertEqual(response.status_code, 200, response.data)

        fetched = Talk.objects.get(id=talk.id)
        self.assertEqual(fetched.title, 'TDD')
        self.assertEqual(fetched.session, self.session)

    def test_update_only_author_can_update_their_talks(self):
        jane = User.objects.create_user('jane@doe.com', 'Jane', 'Doe', 'jd')
        talk = Talk.objects.create(title='Jane Talk',
                                   author=jane,
                                   session=self.session)

        url = reverse('talk-detail', kwargs={'pk': talk.id})
        response = self.client.post(url, {
            'title': 'TDD',
        })

        # we are logged in as Joe so we should not be allowed to change Jane's
        # talk
        self.assertEqual(response.status_code, 404, response.data)

    def test_delete(self):
        talk = Talk.objects.create(title='Joe Talk',
                                   author=self.user,
                                   session=self.session)

        url = reverse('talk-detail', kwargs={'pk': talk.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204, response.data)

    def test_delete_only_author_can_remove_their_talks(self):
        jane = User.objects.create_user('jane@doe.com', 'Jane', 'Doe', 'jd')
        talk = Talk.objects.create(title='Jane Talk',
                                   author=jane,
                                   session=self.session)

        url = reverse('talk-detail', kwargs={'pk': talk.id})
        response = self.client.delete(url)

        # we are logged in as Joe so we should not be allowed to delete Jane's
        # talk
        self.assertEqual(response.status_code, 404, response.data)
