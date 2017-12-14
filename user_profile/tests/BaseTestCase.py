from django.contrib.auth.models import User
from django.test import TestCase, Client


class BestTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('johnathon', 'lennon@thebeatles.com', 'passjohnpass')
        self.user2 = User.objects.create_user('tomas', 'tom@jeff.com', 'passjeffpass')
        self.c = Client()
        self.c.login(username='johnathon', password='passjohnpass')

    def ajax_post(self, url, data):
        return self.c.post(url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
