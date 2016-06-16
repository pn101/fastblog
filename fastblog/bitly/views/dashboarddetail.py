from django.views.generic.list import View
from django.shortcuts import render

from bitly.models import BitLink


class BitLinkDashboardDetailListView(View):

    def get(self, request, *args, **kwargs):
        bitlink = BitLink.objects.get(
                shorten_hash=kwargs.get('shorten_hash')
        )

        return render(
                request,
                'dashboard_detail.html',
                {
                    'site_name': bitlink.original_url,
                    'bitlinklog_list': bitlink.bitlinklog_set.all(),
                }
        )
