from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker

from user_profile.helpers.friend_helpers import make_friends
from user_profile.models import Profile, Friends, FriendRequest, Post, Comment, ChatRoom, Message, UserToChatRoom


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            default=False,
            help='Delete users',
        )

        parser.add_argument(
            '--generate',
            action='store_true',
            default=False,
            help='Generates users',
        )

    def handle(self, *args, **options):
        if options['delete']:
            clear()
        if options['generate']:
            generate()


def generate():
    faker = Faker()
    for i in range(1, 6):
        name = faker.name()
        password = faker.first_name()
        User.objects.create_user(id=i, username=name, email=faker.email(), password=password)
        print('name: {}, pass: {}'.format(name, password))

    # making friends
    for friend_id in range(2, 4):
        make_friends(1, friend_id)


def clear():
    User.objects.all().delete()
    Profile.objects.all().delete()
    Friends.objects.all().delete()
    FriendRequest.objects.all().delete()
    Post.objects.all().delete()
    Comment.objects.all().delete()
    UserToChatRoom.objects.all().delete()
    ChatRoom.objects.all().delete()
    Message.objects.all().delete()
    print('db cleared')
