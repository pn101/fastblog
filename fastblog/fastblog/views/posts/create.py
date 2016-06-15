from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostCreateView(PostBaseView, LoginRequiredMixin, CreateView):
    template_name = 'posts/create.html'
    fields = [
        'title',
        'content',
        'image',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
