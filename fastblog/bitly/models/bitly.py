from django.db import models
from django.contrib.auth.models import User


class BitLink(models.Model):

    user = models.ForeignKey(User)

    original_url = models.URLField()

    shorten_hash = models.CharField(
            max_length=6,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original_url

    def get_absolute_url(self):
        pass
