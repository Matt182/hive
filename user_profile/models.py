from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Friends(Model):
    user_id = models.IntegerField()
    friend_id = models.IntegerField()


class FriendRequest(Model):
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()


def get_friends(self):
    try:
        res = Friends.objects.get(user_id=self.id)
    except:
        res = []
    return res


def is_friend_to(self, friend_id):
    try:
        Friends.objects.get(user_id=self.id, friend_id=friend_id)
    except:
        return False
    return True


def is_request_sended_to(self, person_id):
    try:
        FriendRequest.objects.get(sender_id=self.id, receiver_id=person_id)
    except:
        return False
    return True


def is_request_recieved_from(self, person_id):
    try:
        FriendRequest.objects.get(sender_id=person_id, receiver_id=self.id)
    except:
        return False
    return True


User.add_to_class('get_friends', get_friends)
User.add_to_class('is_friend_to', is_friend_to)
User.add_to_class('is_request_sended_to', is_request_sended_to)
User.add_to_class('is_request_recieved_from', is_request_recieved_from)


def send_friend_request(user_id, person_id):
    pass


def accept_friend_request(user_id, person_id):
    pass


def decline_friend_request(user_id, person_id):
    pass


def delete_friend(user_id, person_id):
    pass
