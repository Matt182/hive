from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model

FRIEND = 1
REQUEST_SEND = 2
REQUEST_RECEIVED = 3
UNRELATED = 4


class Profile(Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    avatar = 0
    bio = 0
    gender = 0
    email = 0
    phone = 0
    birth_date = 0


class Friends(Model):
    user_id = models.IntegerField()
    friend_id = models.IntegerField()

    def __repr__(self):
        return "|user_id: {}, friend_id: {}|".format(self.user_id, self.friend_id)

    def __str__(self):
        return self.__repr__()


class FriendRequest(Model):
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()

    def __repr__(self):
        return "|sender_id: {}, reciever_id: {}|".format(self.sender_id, self.receiver_id)

    def __str__(self):
        return self.__repr__()
