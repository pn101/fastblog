from django.db import models


class BitLinkLog(models.Model):

    bitlink = models.ForeignKey('BitLink')

    created_at = models.DateTimeField(auto_add_now=True)
