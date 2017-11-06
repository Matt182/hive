import json

from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from django.test import TestCase, Client

from user_profile.models import Profile


class UserProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(id=1, name='Tom', email='tom@mail.ru', password='pass')
        Profile.objects.create(id=2, name='Sia', email='sia@mail.ru', password='sias')
        self.c = Client()
        session = self.c.session
        session['user'] = json.dumps(model_to_dict(get_object_or_404(Profile, pk=1)))
        session.save()


    def test_show_profile(self):
        response = self.c.get('/user/')
        print(response)
