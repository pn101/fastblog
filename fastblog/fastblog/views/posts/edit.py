from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostEditView(PostBaseView, LoginRequiredMixin, UpdateView):
    template_name = 'posts/edit.html'
    fields = [
        'title',
        'content',
        'image',
    ]

    def get_context_data(self, **kwargs):
        context = super(PostEditView, self).get_context_data(**kwargs)
        context['site_name'] = 'Edit Fastblog Post'
        return context
