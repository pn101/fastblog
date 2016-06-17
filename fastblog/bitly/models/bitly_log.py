from django.db import models


class BitLinkLog(models.Model):

    bitlink = models.ForeignKey('BitLink')

    created_at = models.DateTimeField(auto_add_now=True)

    http_referr = models.CharField(
            max_length=255,
            blank=True,
            null=True,
    )

    http_user_agent = models.CharField(
            max_length=255,
            blank=True,
            null=True,
    )

    logname = models.CharfField(
            max_length=120,
            blank=True,
            null=True,
    )

    request_addr = models.CharField(
            max_length=31,
            blank=True,
            null=True,
    )

    http_meta_json = models.TextField(
            blank=True,
            null=True,
    )
