from django.views.generic import View
from django.shortcuts import redirect

from fastblog.models import Post, Comment


class PostCommentDeleteView(View):

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs.get('pk'))
        comment = post.comment_set.get(id=self.kwargs.get('comment_id'))
        comment.delete()

        return redirect(post)
