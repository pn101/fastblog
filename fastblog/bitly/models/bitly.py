from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class BitLink(models.Model):

    user = models.ForeignKey(User)

    original_url = models.URLField()

    shorten_hash = models.CharField(
            max_length=6,
    )

    created_at = models.DateTimeField(
            auto_now_add=True,
            blank=True,
            null=True,
    )

    update_at = models.DateTimeField(
            auto_now=True,
            blank=True,
            null=True,
    )

    def __str__(self):
        return self.original_url

    def get_absolute_url(self):
        return reverse(
                'bitly:redirect',
                kwargs={
                    'shorten_hash': self.shorten_hash,
                }
        )
