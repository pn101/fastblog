from django.views.generic.list import ListView

from .base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = 'posts/list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['site_name'] = 'FastBlog Dashboard'
        return context
