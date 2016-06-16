from django.views.generic import View
from django.shortcuts import redirect

from bitly.models import BitLink


class BitLinkRedirectView(View):

    def get(self, request, *args, **kwargs):
        bitlink = BitLink.objects.get(
                shorten_hash=self.kwargs.get('shorten_hash')
        )

        bitlink_log = bitlink.bitlinklog_set.create(
                http_referer=request.META.get('HTTP_REFERER'),
                http_user_agent=request.META.get('HTTP_USER_AGENT'),
                http_remote_addr=request.META.get('REMOTE_ADDR'),
                http_meta_json=str(request.META)
        )

        return redirect(bitlink.original_url)
