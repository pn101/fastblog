from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class PostManager(models.Manager):

    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):

    objects = PostManager()

    user = models.ForeignKey(User)

    title = models.CharField(
            max_length=120,
    )

    content = models.TextField()

    image = models.ImageField()

    is_public = models.BooleanField(
            default=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
                'fastblog:detail',
                kwargs={
                    'pk': self.id,
                }
        )