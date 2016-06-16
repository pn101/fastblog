from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.dispatch import receiver
from django.db.models.signals import post_save
from hashids import Hashids


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
        return reverse(
                'bitly:redirect',
                kwargs={
                    'shorten_hash': self.shorten_hash,
                }
        )


@receiver(post_save, sender=BitLink)
def post_save_bitlink(sender, instance, created, **kwargs):
    if created:
        hashids = Hashids(salt="awesome bitlink", min_length=4)
        instance.shorten_hash = hashids.encode(instance.id)
        instance.save()
