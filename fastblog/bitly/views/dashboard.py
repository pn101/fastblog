from django.views.generic.list import ListView

from bitly.models import BitLink


class BitLinkDashboardView(ListView):
    model = BitLink
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(BitLinkDashboardView, self).get_context_data(**kwargs)
        context['site_name'] = 'Bitly Dashboard'
        return context
