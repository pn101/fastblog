from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import BitLinkBaseView
from hashids import Hashids


class BitLinkCreateView(BitLinkBaseView, LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    fields = [
        'original_url',
    ]
    success_url = '/mypage/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BitLinkCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BitLinkCreateView, self).get_context_data(**kwargs)
        context['site_name'] = 'Bitly'
        return context
