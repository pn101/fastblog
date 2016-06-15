from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Comment(models.Model):

    post = models.ForeignKey('Post')

    user = models.ForeignKey(User)

    content = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
                'fastblog:detail',
                kwargs={
                    'pk': self.post.id,
                }
        ) + '#comment-' + str(self.id)
