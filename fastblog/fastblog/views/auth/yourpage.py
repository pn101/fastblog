from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from fastblog.models import Post


class YourPageView(LoginRequiredMixin, TemplateView):
    template_name = 'auth/yourpage.html'

    def get_context_data(self, **kwargs):
        context = super(YourPageView, self).get_context_data(**kwargs)
        context['site_name'] = User.objects.get(username=self.kwargs.get('user_name')).username
        context['post_list'] = User.objects.get(username=self.kwargs.get('user_name')).post_set.all()
        context['comment_list'] = User.objects.get(username=self.kwargs.get('user_name')).comment_set.all()
        context['bitlink_list'] = User.objects.get(username=self.kwargs.get('user_name')).bitlink_set.all()
        return context
