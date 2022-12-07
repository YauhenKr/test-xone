from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from user.signals import post_save_user


class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class Account(models.Model):
    balance = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.balance}'


post_save.connect(post_save_user, sender=User)
