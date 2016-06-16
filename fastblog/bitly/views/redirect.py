from django.views.generic import View
from django.shortcuts import redirect

from bitly.models import BitLink


class BitLinkRedirectView(View):

    def get(self, request, *args, **kwargs):
        bitlink = BitLink.objects.get(
                shorten_hash=self.kwargs.get('shorten_hash')
        )

        return redirect(bitlink.original_url)
