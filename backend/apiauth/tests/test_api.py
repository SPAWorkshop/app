from apiauth.models import User
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


class TestRegisterToLoginFlow(APITestCase):

    def setUp(self):
        self.url = reverse('register')

    def test_register(self):
        """
        - send email and password to /register
        - expect HTTP 201 (user is created)
        - ensure user is created
        - ensure auth token is assigned to created user
        """
        response = self.client.post(self.url, {
            'email': 'joe@doe.com',
            'password': 's3cr3t',
        })

        self.assertEqual(response.status_code, 201)
        user = User.objects.get(email='joe@doe.com')
        self.assertTrue(user.check_password('s3cr3t'))

    def test_register_user_exists(self):
        """
        - send email and password to /register
        - expect HTTP 400 (cannot register user that already exists)
        - expect 'email' in returned json
        """
        User.objects.create_user('joe@doe.com', 's3cr3t')

        response = self.client.post(self.url, {
            'email': 'joe@doe.com',
            'password': 's3cret3',
        })

        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data)

    def test_register_wrong_email(self):
        """
        - send email and password to /register but with malformed email value
        - expect HTTP 400
        - expect 'email' in returned json
        """
        response = self.client.post(self.url, {
            'email': 'joe@doe',
            'password': 's3cret3',
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data)

    def test_register_missing_email(self):
        """
        - send password to /register (no email)
        - expect HTTP 400
        - expect 'email' in returned json
        """
        response = self.client.post(self.url, {
            'password': 's3cret3',
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data)

    def test_register_missing_password(self):
        """
        - send email to /register (no password)
        - expect HTTP 400
        - expect 'password' in returned json
        """
        response = self.client.post(self.url, {
            'email': 'joe@doe.com',
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.data)


class TestLogin(APITestCase):

    def setUp(self):
        self.url = reverse('login')

    def test_login(self):
        """
        - create active user
        - send user's email and password to /login
        - expect HTTP 200 and 'token' value (that user can use for further API
          calls)
        """

    def test_login_wrong_password(self):
        """
        - create active user
        - send user's email and password to /login
        - expect HTTP 200 and 'token' value (that user can use for further API
          calls)
        """

    def test_login_inactive_user(self):
        """
        - create active user
        - send user's email and password to /login
        - expect HTTP 200 and 'token' value (that user can use for further API
          calls)
        """

    def test_login_wrong_email(self):
        """
        - create active user
        - send user's email and password to /login
        - expect HTTP 200 and 'token' value (that user can use for further API
          calls)
        """
