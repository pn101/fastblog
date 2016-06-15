from django.views.generic import View

from fastblog.models import Comment


class CommentBaseView(View):
    model = Comment
