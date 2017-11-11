from django.contrib.auth.models import User
from django.test import TestCase, Client


# Create your tests here.
HTTP_REDIRECT = 302
HTTP_OK = 200

class UserProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        User.objects.create_user('tom', 'tom@jeff.com', 'jeffpass')
        self.c = Client()

    def test_login(self):
        response = self.c.get('/user/')
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get('/')
        self.assertEqual(response.status_code, HTTP_OK)
        response = self.c.post('/login/', {
            'username': 'tom',
            'password': 'jeffpass',
        })
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get('/user/')
        self.assertEqual(response.status_code, HTTP_OK)
        response = self.c.get('/')
        self.assertEqual(response.status_code, HTTP_REDIRECT)

    def test_logout(self):
        response = self.c.post('/login/', {
            'username': 'tom',
            'password': 'jeffpass',
        })
        response = self.c.get('/')
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get('/logout/')
        response = self.c.get('/')
        self.assertEqual(response.status_code, HTTP_OK)
        response = self.c.get('/user/')
        self.assertEqual(response.status_code, HTTP_REDIRECT)

    def test_registration(self):
        response = self.c.get('/user/')
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        response = self.c.get('/registration/')
        print(response)
        self.assertEqual(response.status_code, HTTP_OK)
        response = self.c.post('/registration/', {
            'username': 'new_user',
            'email': 'new_user@email.com',
            'password': 'new_user_pass',
        })
        print(response)
