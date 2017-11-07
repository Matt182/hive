from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField

    def friends(self):
        return Friends.objects.get(user_id=self.user.id)


class Friends(Model):
    user_id = models.IntegerField()
    friend_id = models.IntegerField()
