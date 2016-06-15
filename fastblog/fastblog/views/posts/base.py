from django.views.generic import View

from fastblog.models import Post


class PostBaseView(View):
    model = Post
