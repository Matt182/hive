import json

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from user_profile.models import FriendRequest, Friends

HTTP_REDIRECT = 302


class UserProfileTestCase(TestCase):

    post_send_friend_request = reverse('send_friend_request')
    post_decline_received_friend_request = reverse('decline_received_friend_request')
    post_accept_friend_request = reverse('accept_friend_request')

    def setUp(self):
        self.user1 = User.objects.create_user('johnathon', 'lennon@thebeatles.com', 'passjohnpass')
        self.user2 = User.objects.create_user('tomas', 'tom@jeff.com', 'passjeffpass')
        self.c = Client()
        self.c.login(username='johnathon', password='passjohnpass')

    def ajax_post(self, url, data):
        return self.c.post(url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

    @staticmethod
    def is_no_row(model, kwargs):
        try:
            model.objects.get(kwargs)
            return False
        except:
            return True

    def test_send_and_decline_friend_request(self):
        response = self.ajax_post(self.post_send_friend_request, {'person_id': self.user2.id})
        resp_content = json.loads(response.content.decode('utf-8'))
        self.assertAlmostEqual('success', resp_content['result'])
        req = FriendRequest.objects.get(sender_id=self.user1.id, receiver_id=self.user2.id)
        self.assertIsNotNone(req)
        self.c.logout()

        self.c.login(username='tomas', password='passjeffpass')
        response = self.ajax_post(self.post_decline_received_friend_request, {'person_id': self.user1.id})
        resp_content = json.loads(response.content.decode('utf-8'))
        self.assertAlmostEqual('success', resp_content['result'])
        self.assertTrue(self.is_no_row(FriendRequest, {'sender_id':self.user1.id, 'receiver_id':self.user2.id}))

    def test_send_and_accept_friend_request(self):
        response = self.ajax_post(self.post_send_friend_request, {'person_id': self.user2.id})
        resp_content = json.loads(response.content.decode('utf-8'))
        self.assertAlmostEqual('success', resp_content['result'])
        req = FriendRequest.objects.get(sender_id=self.user1.id, receiver_id=self.user2.id)
        self.assertIsNotNone(req)
        self.c.logout()

        self.c.login(username='tomas', password='passjeffpass')
        response = self.ajax_post(self.post_accept_friend_request, {'person_id': self.user1.id})
        resp_content = json.loads(response.content.decode('utf-8'))
        self.assertAlmostEqual('success', resp_content['result'])
        self.assertTrue(self.is_no_row(FriendRequest, {'sender_id': self.user1.id, 'receiver_id': self.user2.id}))
        friendship1 = Friends.objects.get(user_id=self.user1.id, friend_id=self.user2.id)
        friendship2 = Friends.objects.get(user_id=self.user2.id, friend_id=self.user1.id)
        self.assertIsNotNone(friendship1)
        self.assertIsNotNone(friendship2)

        def test_delete_friend(self):
            self.ajax_post('send_friend_request', {'person_id': self.user2.id})
            self.c.logout()
            self.c.login(username='tomas', password='passjeffpass')
            self.ajax_post('accept_friend_request', {'person_id': self.user1.id})

            response = self.ajax_post('delete_friend', {'person_id': self.user1.id})
            resp_content = json.loads(response.content.decode('utf-8'))
            self.assertAlmostEqual('success', resp_content['result'])

            self.assertTrue(self.is_no_row(Friends, {'user_id': self.user1.id, 'friend_id': self.user2.id}))
            self.assertTrue(self.is_no_row(Friends, {'user_id': self.user2.id, 'friend_id': self.user1.id}))
