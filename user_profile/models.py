from django.contrib.auth.models import User
from django.core import serializers
from django.db import models
from django.db.models import Model

FRIEND = 1
REQUEST_SEND = 2
REQUEST_RECEIVED = 3
UNRELATED = 4

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'


def get_deleted_user():
    return User.objects.get_or_create(username='deleted')[0]


def user_directory_path(instance, filename):
    return 'user_{}/avatar_{}'.format(instance.user.id, filename)


class Profile(Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    avatar = models.FileField(upload_to=user_directory_path)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)


class ChatRoom(Model):
    TYPE_PAIR = 'pair'
    TYPE_GROUP = 'group'

    last_message_id = models.IntegerField(default=0)
    type = models.CharField(max_length=15)

    def __repr__(self):
        return "|chat_room_id: {}|".format(self.pk)

    def __str__(self):
        return self.__repr__()


class UserToPairChatRoom(Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_user_id'
    )
    pair = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_pair_id'
    )
    chat_room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
    )


class UserToChatRoom(Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    chat_room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
    )


class Friends(Model):
    user_id = models.IntegerField()
    friend = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

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


class Message(Model):
    message = models.TextField()
    chat_room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET(get_deleted_user),
    )
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET(get_deleted_user),
    )
    owner_id = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "|author_id: {}, owner_id: {}. message: {}|".format(self.author.id, self.owner_id, self.message)

    def __str__(self):
        return self.__repr__()

    def to_json(self):
        return serializers.serialize('json', [self], fields=('owner_id', 'author_id', 'created_at'))


class Comment(Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    message = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.SET(get_deleted_user),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "|author_id: {}, post_id: {}. message: {}|".format(self.author.id, self.post_id, self.message)

    def __str__(self):
        return self.__repr__()

    def to_json(self):
        return serializers.serialize('json', [self], fields=('post_id', 'author_id', 'message', 'created_at'))
