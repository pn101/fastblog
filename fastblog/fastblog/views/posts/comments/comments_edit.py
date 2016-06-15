from django.views.generic import View
from django.shortcuts import render, redirect

from .base import CommentBaseView
from fastblog.models import Post, Comment


class PostCommentEditView(CommentBaseView, View):

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(
                id=self.kwargs.get('pk')
        )
        comment = post.comment_set.get(
                id=self.kwargs.get('comment_id')
        )

        return render(
                request,
                'posts/comment_edit.html',
                {
                    'post': post,
                    'comment': comment,
                }
        )

    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')

        post = Post.objects.get(
                id=self.kwargs.get('pk')
        )
        comment = post.comment_set.get(
                id=self.kwargs.get('comment_id')
        )

        comment.content = content
        comment.save()

        return redirect(comment)
