from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model

FRIEND = 1
REQUEST_SEND = 2
REQUEST_RECEIVED = 3
UNRELATED = 4

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'


def user_directory_path(instance, filename):
    return 'user_{}/avatar_{}'.format(instance.user.id, filename)


class Profile(Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    avatar = models.FileField(upload_to=user_directory_path)
    bio = models.TextField()
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()


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
        return "|sender_id: {}, receiver_id: {}|".format(self.sender_id, self.receiver_id)

    def __str__(self):
        return self.__repr__()
