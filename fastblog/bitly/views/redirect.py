from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404


class BitLinkRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        bitlink = get_object_or_404(
                self.request.user.bitlink_set,
                shorten_hash=kwargs.get('shorten_hash'),
        )
        return bitlink.original_url
