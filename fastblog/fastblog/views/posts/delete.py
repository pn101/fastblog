from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostDeleteView(PostBaseView, LoginRequiredMixin, DeleteView):
    template_name = 'posts/delete_confirmation.html'
    success_url = reverse_lazy('fastblog:list')
