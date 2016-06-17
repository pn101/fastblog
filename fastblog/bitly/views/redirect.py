from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404


class BitLinkRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        bitlink = get_object_or_404(
                self.request.user.bitlink_set,
                shorten_hash=self.kwargs.get('shorten_hash'),
        )

        bitlinklog = bitlink.bitlinklog_set.create(
                http_referer=request.META.get('HTTP_REFERER'),
                http_user_agent=request.META.get('HTTP_USER_AGENT'),
                logname=request.META.get('LOGNAME'),
                remote_addr=request.META.get('REMOTE_ADDR'),
        )

        return bitlink.original_url
