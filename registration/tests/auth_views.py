
import simplejson as json

from django.core.urlresolvers import reverse
from django.contrib.auth import SESSION_KEY
from django.contrib.auth.tests.views import AuthViewsTestCase

from django.test import TestCase


class AuthViewsJsonTestCase(AuthViewsTestCase):

    urls = 'registration.auth_urls'

    def login(self, password='password'):
        response = self.client.post(reverse('auth_login'), {
            'username': 'testclient',
            'password': password
            },
            **{'HTTP_ACCEPT':'application/json'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['success'])
        self.assertTrue(SESSION_KEY in self.client.session)

    def fail_login(self, password='password'):
        response = self.client.post(reverse('auth_login'), {
            'username': 'testclient',
            'password': password
            },
            **{'HTTP_ACCEPT':'application/json'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(json.loads(response.content)['success'])
        self.assertTrue(u"Please enter a correct username and password. Note that both fields are case-sensitive." in json.loads(response.content)['errors'])
        self.assertFalse(SESSION_KEY in self.client.session)

class SigninTestCase(AuthViewsJsonTestCase):

    def test_successful_login(self):
        self.login()

    def test_fail_login(self):
        self.fail_login(password='donuts')

