from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models import Model

FRIEND = 1
REQUEST_SENDED = 2
REQUEST_RECIEVED = 3
UNRELATED = 4


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


def get_relation_to(self, person_id):
    if self.is_friend_to(person_id):
        return FRIEND
    if self.is_request_sended_to(person_id):
        return REQUEST_SENDED
    if self.is_request_recieved_from(person_id):
        return REQUEST_RECIEVED
    return UNRELATED


User.add_to_class('get_friends', get_friends)
User.add_to_class('is_friend_to', is_friend_to)
User.add_to_class('is_request_sended_to', is_request_sended_to)
User.add_to_class('is_request_recieved_from', is_request_recieved_from)
User.add_to_class('get_relation_to', get_relation_to)


def send_friend_request(user_id, person_id):
    req = FriendRequest(user_id=user_id, person_id=person_id)
    req.save()


@transaction.atomic
def accept_friend_request(user_id, person_id):
    req = FriendRequest.objects.get(sender_id=person_id, receiver_id=user_id)
    req.delete()
    Friends(user_id=user_id, friend_id=person_id).save()
    Friends(user_id=person_id, friend_id=user_id).save()


def decline_friend_request(user_id, person_id):
    req = FriendRequest.objects.get(sender_id=person_id, receiver_id=user_id)
    req.delete()


@transaction.atomic
def delete_friend(user_id, person_id):
    Friends(user_id=user_id, friend_id=person_id).delete()
    Friends(user_id=person_id, friend_id=user_id).delete()
