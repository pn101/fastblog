from django.views.generic.list import ListView

from bitly.models import BitLink


class BitLinkDashboardView(ListView):
    model = BitLink
    template_name = 'dashboard.html'
    context_object_name = 'bitlink'

    def get_queryset(self):
        bitlink = self.model.objects.get(
                shorten_hash=self.kwargs.get('shorten_hash')
        )

        return bitlink
