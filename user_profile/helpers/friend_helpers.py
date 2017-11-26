from django.db import transaction

from user_profile.models import Friends, FriendRequest, FRIEND, REQUEST_SEND, UNRELATED, REQUEST_RECEIVED


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


def is_request_send_to(user_id, person_id):
    try:
        FriendRequest.objects.get(sender_id=user_id, receiver_id=person_id)
    except:
        return False
    return True


def is_request_received_from(user_id, person_id):
    try:
        FriendRequest.objects.get(sender_id=person_id, receiver_id=user_id)
    except:
        return False
    return True


def get_relation_to(user_id, person_id):
    if is_friend_to(user_id, person_id):
        return FRIEND
    if is_request_send_to(user_id, person_id):
        return REQUEST_SEND
    if is_request_received_from(user_id, person_id):
        return REQUEST_RECEIVED
    return UNRELATED


def send_friend_request(user_id, person_id):
    req = FriendRequest(sender_id=user_id, receiver_id=person_id)
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
    friendship = Friends.objects.get(user_id=user_id, friend_id=person_id)
    friendship.delete()
    friendship = Friends.objects.get(user_id=person_id, friend_id=user_id)
    friendship.delete()