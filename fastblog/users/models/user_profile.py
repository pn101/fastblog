from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    phonenumber = models.CharField(
            max_length=16,
            blank=True,
            null=True,
    )

    address = models.CharField(
            max_length=64,
            blank=True,
            null=True,
    )
