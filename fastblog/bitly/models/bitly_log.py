from django.db import models


class BitLinkLog(models.Model):

    bitlink = models.ForeignKey('BitLink')

    created_at = models.DateTimeField(auto_now_add=True)

    http_referer = models.CharField(
            max_length=255,
            blank=True,
            null=True,
    )

    http_user_agent = models.CharField(
            max_length=255,
            blank=True,
            null=True,
    )

    logname = models.CharField(
            max_length=120,
            blank=True,
            null=True,
    )

    remote_addr = models.CharField(
            max_length=31,
            blank=True,
            null=True,
    )

    http_meta_json = models.TextField(
            blank=True,
            null=True,
    )
