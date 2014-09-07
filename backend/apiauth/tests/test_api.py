from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


class TestRegisterToLoginFlow(APITestCase):

    def setUp(self):
        self.url = reverse('register')

    def test_register(self):
        """
        - send email and password to /register
        - expect HTTP 201 (from the client point of view it creates a
          activation token)
        - ensure we email is sent with activation link
        """

    def test_register_user_exists(self):
        """
        - send email and password to /register
        - expect HTTP 400 (cannot register user that already exists)
        """

    def test_register_wrong_email(self):
        """
        - send email and password to /register but with malformed email value
        - expect HTTP 400
        """


class TestActivate(APITestCase):

    def setUp(self):
        self.url = reverse('activate')

    def test_activate(self):
        """
        - create user and activation token
        - send token value to /activate
        - expect HTTP 201 (from the client point of view it creates an user)
        - ensure user.is_active
        """

    def test_activate_wrong_token(self):
        """
        - create user and activation token
        - send wrong token value to /activate
        - expect HTTP 201 (from the client point of view it creates an user)
        - ensure user.is_active
        - ensure activation token is not reusable (send token again and expect
          HTTP 400)
        """

    def test_activate_reuse_token(self):
        """
        - create inactive user
        - create activation token for that user and mark it as already used
        - send token value to /activate
        - expect HTTP 400 ("This user was already activated")
        """


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
