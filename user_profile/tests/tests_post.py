import json

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from user_profile.models import Friends, Post
from user_profile.tests.BaseTestCase import BestTestCase


class PostTestCase(BestTestCase):
    post_send_friend_post = reverse('send_post')

    def setUp(self):
        super().setUp()
        Friends(user_id=self.user1.id, friend_id=self.user2.id).save()
        Friends(user_id=self.user2.id, friend_id=self.user1.id).save()

    def test_create_friend_post(self):
        msg = "Hello my friend"
        response = self.ajax_post(self.post_send_friend_post, {
            'wall_owner_id': self.user2.id,
            'message': msg,
        })
        resp_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual('success', resp_content['result'])
        post = Post.objects.get(owner_id=self.user2.id, author_id=self.user1.id)
        self.assertIsNotNone(post)
        self.assertEqual(post.message, msg)
        msg2 = "Hello again"
        response = self.ajax_post(self.post_send_friend_post, {
            'wall_owner_id': self.user2.id,
            'message': msg2,
        })
        resp_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual('success', resp_content['result'])
        posts = Post.objects.filter(owner_id=self.user2.id, author_id=self.user1.id)
        self.assertIsNotNone(posts)
        self.assertEqual(len(posts), 2)
