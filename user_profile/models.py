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
    reciever_id = models.IntegerField()


def get_friends(user_id):
    try:
        res = Friends.objects.get(user_id=user_id)
    except:
        res = []
    return res


def is_friend_to(user_id, friend_id):
    try:
        Friends.objects.get(user_id=user_id, friend_id=friend_id)
    except:
        return False
    return True


def is_request_sended_to(user_id, person_id):
    try:
        FriendRequest.objects.get(sender_id=user_id, reciever_id=person_id)
    except:
        return False
    return True


def is_request_recieved_from(user_id, person_id):
    try:
        FriendRequest.objects.get(sender_id=person_id, reciever_id=user_id)
    except:
        return False
    return True


def get_relation_to(user_id, person_id):
    if is_friend_to(user_id, person_id):
        return FRIEND
    if is_request_sended_to(user_id, person_id):
        return REQUEST_SENDED
    if is_request_recieved_from(user_id, person_id):
        return REQUEST_RECIEVED
    return UNRELATED


def send_friend_request(user_id, person_id):
    req = FriendRequest(sender_id=user_id, reciever_id=person_id)
    req.save()


@transaction.atomic
def accept_friend_request(user_id, person_id):
    req = FriendRequest.objects.get(sender_id=person_id, reciever_id=user_id)
    req.delete()
    Friends(user_id=user_id, friend_id=person_id).save()
    Friends(user_id=person_id, friend_id=user_id).save()


def decline_friend_request(user_id, person_id):
    req = FriendRequest.objects.get(sender_id=person_id, reciever_id=user_id)
    req.delete()


@transaction.atomic
def delete_friend(user_id, person_id):
    Friends(user_id=user_id, friend_id=person_id).delete()
    Friends(user_id=person_id, friend_id=user_id).delete()
