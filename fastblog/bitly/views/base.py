from django.views.generic import View

from bitly.models import BitLink


class BitLinkBaseView(View):
    model = BitLink
