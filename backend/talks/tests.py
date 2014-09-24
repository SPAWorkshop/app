from accounts.models import User
from django.core.urlresolvers import reverse
from lightningtalks.utils import utc_datetime
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from talks.models import Session
from talks.models import Talk


class TestSesssionAPI(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('joe@doe.com', 'Joe', 'Doe', 'pwd')
        self.admin = User.objects.create_user('admin@foo.com', 'Admin', '', 'pwd',
                                              is_staff=True)
        self.token = Token.objects.create(user=self.user)
        self.admin_token = Token.objects.create(user=self.admin)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        Session.objects.create(name='S1', starts_at=utc_datetime(2014, 10, 15, 19))
        Session.objects.create(name='S2', starts_at=utc_datetime(2014, 10, 16, 19))
        Session.objects.create(name='S3', starts_at=utc_datetime(2014, 10, 17, 19))

    def test_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('session-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(set([s['name'] for s in response.data]),
                         set(['S1', 'S2', 'S3']))

    def test_list_unauthorized(self):
        response = self.client.get(reverse('session-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(set([s['name'] for s in response.data]),
                         set(['S1', 'S2', 'S3']))

    def test_create_should_fail_for_normal_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('session-list'), {
            'name': 'LH Session',
            'starts_at': '2014-10-20T20:00:00Z',
        })
        self.assertEqual(response.status_code, 405, response.data)

    def test_get(self):
        session = Session.objects.get(name='S1')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('session-detail', kwargs={'pk': session.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response.data)

    def test_get_unauthorized(self):
        session = Session.objects.get(name='S1')
        url = reverse('session-detail', kwargs={'pk': session.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, response.data)

    def test_update_should_fail_for_normal_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        session = Session.objects.get(name='S1')
        url = reverse('session-detail', kwargs={'pk': session.pk})
        response = self.client.post(url, {'name': 'Foo sessions'})
        self.assertEqual(response.status_code, 405, response.data)

    def test_delete_should_fail_for_normal_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        session = Session.objects.get(name='S1')
        url = reverse('session-detail', kwargs={'pk': session.pk})
        response = self.client.delete(url, {'name': 'Foo sessions'})
        self.assertEqual(response.status_code, 405, response.data)


class TestTalkAPI(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('joe@doe.com', 'Joe', 'Doe', 'pwd')
        self.token = Token.objects.create(user=self.user)
        self.session = Session.objects.create(
            name='LH Session',
            starts_at=utc_datetime(2014, 10, 15, 19),
            max_talks=2,
        )
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list(self):
        Talk.objects.create(title='T1', author=self.user, session=self.session)
        Talk.objects.create(title='T2', author=self.user, session=self.session)
        jane = User.objects.create_user('jane@doe.com', 'Jane', 'Doe', 'jd')
        Talk.objects.create(title='T3', author=jane, session=self.session)

        response = self.client.get(reverse('talk-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(set([t['title'] for t in response.data]),
                         set(['T1', 'T2']))

    def test_create(self):
        response = self.client.post(reverse('talk-list'), {
            'session': self.session.id,
            'title': 'Joe Talk',
        })

        self.assertEqual(response.status_code, 201)

        talk = Talk.objects.get(title='Joe Talk')
        self.assertEqual(talk.author, self.user)

    def test_create_unauthorized(self):
        self.client.credentials()  # clear headers
        response = self.client.post(reverse('talk-list'), {
            'session': self.session.id,
            'title': 'Joe Talk',
        })
        self.assertEqual(response.status_code, 401)

    def test_create_cannot_exceed_over_session_limit(self):
        Talk.objects.create(title='T1', author=self.user, session=self.session)
        Talk.objects.create(title='T2', author=self.user, session=self.session)

        response = self.client.post(reverse('talk-list'), {
            'session': self.session.id,
            'title': 'Joe Talk',
        })

        self.assertEqual(response.status_code, 400, response.data)
        self.assertIn('session', response.data)

    def test_get(self):
        talk = Talk.objects.create(title='Joe Talk',
                                   author=self.user,
                                   session=self.session)

        url = reverse('talk-detail', kwargs={'pk': talk.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertDictEqual(response.data, {
            'id': talk.id,
            'title': 'Joe Talk',
            'session': talk.session_id,
            'author': {
                'first_name': 'Joe',
                'last_name': 'Doe',
            },
        })

    def test_update(self):
        talk = Talk.objects.create(title='Joe Talk',
                                   author=self.user,
                                   session=self.session)

        url = reverse('talk-detail', kwargs={'pk': talk.id})
        response = self.client.put(url, {
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
        response = self.client.put(url, {
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
        response = self.client.put(url, {
            'title': 'TDD',
        })

        # we are logged in as Joe so we should not be allowed to change Jane's
        # talk
        self.assertEqual(response.status_code, 403, response.data)

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
        self.assertEqual(response.status_code, 403, response.data)
