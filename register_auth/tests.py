from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
HTTP_REDIRECT = 302
HTTP_OK = 200


class UserProfileTestCase(TestCase):
    get_user_url = '/user/'
    get_login_url = '/'
    get_logout_url = '/logout/'
    registration_url = '/registration/'
    post_login_url = '/login/'


    def setUp(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        User.objects.create_user('tom', 'tom@jeff.com', 'jeffpass')
        self.c = Client()

    def test_login(self):
        response = self.c.get(self.get_user_url)
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get(self.get_login_url)
        self.assertEqual(response.status_code, HTTP_OK)
        response = self.c.post(self.post_login_url, {
            'username': 'tom',
            'password': 'jeffpass',
        })
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get(self.get_user_url)
        self.assertEqual(response.status_code, HTTP_OK)
        response = self.c.get(self.get_login_url)
        self.assertEqual(response.status_code, HTTP_REDIRECT)

    def test_logout(self):
        response = self.c.post(self.post_login_url, {
            'username': 'tom',
            'password': 'jeffpass',
        })
        response = self.c.get(self.get_login_url)
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get(self.get_logout_url)
        response = self.c.get(self.get_login_url)
        self.assertEqual(response.status_code, HTTP_OK)
        response = self.c.get(self.get_user_url)
        self.assertEqual(response.status_code, HTTP_REDIRECT)

    def test_registration(self):
        new_username = 'new_user'
        new_user_email = 'new_user@email.com'
        new_user_password = 'new_user_pass'

        response = self.c.get(self.get_user_url)
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get(self.registration_url)
        self.assertEqual(response.status_code, HTTP_OK)
        response = self.c.post(self.registration_url, {
            'username': new_username,
            'email': new_user_email,
            'password': new_user_password,
        })
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get(self.get_user_url)
        self.assertEqual(response.status_code, HTTP_OK)
        registered = User.objects.get(username=new_username)
        self.assertIsNotNone(registered)
        self.assertEqual(registered.email, new_user_email)
