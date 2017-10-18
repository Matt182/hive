from django.test import TestCase, Client

from user_profile.models import User


class UserProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=1, name='Tom', email='tom@mail.ru', password='pass')
        User.objects.create(id=2, name='Sia', email='sia@mail.ru', password='sias')


    def test_show_profile(self):
        c = Client()
        c.get('/user/')