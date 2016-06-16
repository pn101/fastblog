from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import CommentBaseView
from fastblog.models import Post


class PostCommentCreateView(CommentBaseView, LoginRequiredMixin, CreateView):
    template_name = 'posts/detail.html'
    fields = [
        'content',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(
                id=self.kwargs.get('pk')
        )

        return super(PostCommentCreateView, self).form_valid(form)
