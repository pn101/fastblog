from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from hashids import Hashids

from bitly.models import BitLink


class BitLinkCreateView(LoginRequiredMixin, CreateView):
    model = BitLink
    template_name = 'bitly.html'
    fields = [
        'original_url',
    ]
    success_url = '/mypage/'

    def form_valid(self, form):
        hashids = Hashids(salt="awesome bitlink", min_length=4)
        form.instance.user = self.request.user
        form.save()
        form.instance.shorten_hash = hashids.encode(
                form.instance.id,
        )

        return super(BitLinkCreateView, self).form_valid(form)
