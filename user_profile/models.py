from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


def get_friends(self):
    try:
        res = Friends.objects.get(user_id=self.id)
    except:
        res = []
    return res


User.add_to_class('get_friends', get_friends)


class Friends(Model):
    user_id = models.IntegerField()
    friend_id = models.IntegerField()
