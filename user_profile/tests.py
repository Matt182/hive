from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from user_profile.models import FriendRequest, Friends

HTTP_REDIRECT = 302


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('johnathon', 'lennon@thebeatles.com', 'passjohnpass')
        self.user2 = User.objects.create_user('tomas', 'tom@jeff.com', 'passjeffpass')
        self.c = Client()
        self.c.login(username='johnathon', password='passjohnpass')

    def test_send_and_decline_friend_request(self):
        response = self.c.post(reverse('send_friend_request', kwargs={'person_id': self.user2.id}))
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        req = FriendRequest.objects.get(sender_id=self.user1.id, reciever_id=self.user2.id)
        self.assertIsNotNone(req)
        self.c.logout()
        self.c.login(username='tomas', password='passjeffpass')
        response = self.c.post(reverse('decline_received_friend_request', kwargs={'person_id': self.user1.id}))
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        try:
            FriendRequest.objects.get(sender_id=self.user1.id, reciever_id=self.user2.id)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_send_and_accept_friend_request(self):
        response = self.c.post(reverse('send_friend_request', kwargs={'person_id': self.user2.id}))
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        req = FriendRequest.objects.get(sender_id=self.user1.id, reciever_id=self.user2.id)
        self.assertIsNotNone(req)
        self.c.logout()
        self.c.login(username='tomas', password='passjeffpass')
        response = self.c.post(reverse('accept_friend_request', kwargs={'person_id': self.user1.id}))
        self.assertEqual(response.status_code, HTTP_REDIRECT)
        try:
            FriendRequest.objects.get(sender_id=self.user1.id, reciever_id=self.user2.id)
            self.assertTrue(False)
        except:
            self.assertTrue(True)
        friendship1 = Friends.objects.get(user_id=self.user1.id, friend_id=self.user2.id)
        friendship2 = Friends.objects.get(user_id=self.user2.id, friend_id=self.user1.id)
        self.assertIsNotNone(friendship1)
        self.assertIsNotNone(friendship2)

    def test_delete_friend(self):
        self.c.post(reverse('send_friend_request', kwargs={'person_id': self.user2.id}))
        self.c.logout()
        self.c.login(username='tomas', password='passjeffpass')
        self.c.post(reverse('accept_friend_request', kwargs={'person_id': self.user1.id}))

        response = self.c.post(reverse('delete_friend', kwargs={'person_id': self.user1.id}))
        self.assertEqual(response.status_code, HTTP_REDIRECT)

        try:
            Friends.objects.get(user_id=self.user1.id, friend_id=self.user2.id)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

        try:
            Friends.objects.get(user_id=self.user2.id, friend_id=self.user1.id)
            self.assertTrue(False)
        except:
            self.assertTrue(True)
