from django.views.generic.list import ListView

from bitly.models import BitLink


class BitLinkDashboardView(ListView):
    model = BitLink
    template_name = 'dashboard.html'
