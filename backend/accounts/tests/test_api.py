from accounts import constants
from accounts.models import User
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from unittest import mock


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

    @mock.patch.object(Token, 'generate_key', lambda self: 'TOKEN')
    def test_login(self):
        """
        - create active user
        - send user's email and password to /login
        - expect HTTP 200 and 'token' value (that user can use for further API
          calls)
        - check that authtoken.Token was created for the user
        """
        user = User.objects.create_user('joe@doe.com', 's3cr3t')

        response = self.client.post(self.url, {
            'email': 'joe@doe.com',
            'password': 's3cr3t',
        })
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, {'token': 'TOKEN'})

        token = Token.objects.get(user=user)
        self.assertEqual(token.key, 'TOKEN')

    def test_login_wrong_password(self):
        """
        - create active user
        - send user's email and password to /login
        - expect HTTP 400
        - expect 'non_TODO' in returned json
        """
        User.objects.create_user('joe@doe.com', 's3cr3t')
        response = self.client.post(self.url, {
            'email': 'joe@doe.com',
            'password': 'secret',
        })
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.data, {
            'non_field_errors': [constants.INVALID_CREDENTIALS_ERROR],
        })

    def test_login_inactive_user(self):
        """
        - create inactive user
        - send user's email and password to /login
        - expect HTTP 400 and 'non_field_errors' in returned json
        """
        User.objects.create_user('joe@doe.com', 's3cr3t', is_active=False)
        response = self.client.post(self.url, {
            'email': 'joe@doe.com',
            'password': 's3cr3t',
        })
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.data, {
            'non_field_errors': [constants.INACTIVE_ACCOUNT_ERROR],
        })

    def test_login_missing_email(self):
        """
        - send password to /login (no email)
        - expect HTTP 400
        - expect 'email' in returned json
        """
        response = self.client.post(self.url, {
            'password': 's3cret3',
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data)

    def test_login_missing_password(self):
        """
        - send email to /login (no password)
        - expect HTTP 400
        - expect 'password' in returned json
        """
        response = self.client.post(self.url, {
            'email': 'joe@doe.com',
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.data)


class TestProfile(APITestCase):

    def setUp(self):
        self.url = reverse('profile')

    def test_profile(self):
        user = User.objects.create_user('joe@doe.com', 's3cr3t')
        token, created = Token.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, {
            'email': 'joe@doe.com',
        })

    def test_profile_not_authed_user(self):
        User.objects.create_user('joe@doe.com', 's3cr3t')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 401)
