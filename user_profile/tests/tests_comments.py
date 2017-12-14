import json

from django.urls import reverse

from user_profile.models import Post, Comment
from user_profile.tests.BaseTestCase import BestTestCase


class CommentsTestCase(BestTestCase):
    post_leave_comment = reverse('leave_comment')

    def setUp(self):
        super().setUp()
        self.post = Post(author_id=self.user1.id, owner_id=self.user2.id, message='hi')
        self.post.save()

    def test_create_comment(self):
        msg = 'Comment to post'
        response = self.ajax_post(self.post_leave_comment, {
            'post_id': self.post.id,
            'author_id': self.user1.id,
            'message': msg,
        })
        resp_content = json.loads(response.content.decode('utf-8'))
        self.assertAlmostEqual('success', resp_content['result'])
        posts = Comment.objects.filter(post_id=self.post.id)
        self.assertEqual(len(posts), 1)

        msg2 = 'Another Comment'
        response = self.ajax_post(self.post_leave_comment, {
            'post_id': self.post.id,
            'author_id': self.user2.id,
            'message': msg2,
        })
        self.assertAlmostEqual('success', resp_content['result'])
        posts = Comment.objects.filter(post_id=self.post.id)
        self.assertEqual(len(posts), 2)
