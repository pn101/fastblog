from django.views.generic import TemplateView


class MyPageView(TemplateView):
    template_name = 'auth/mypage.html'

    def get_context_data(self, **kwargs):
        context = super(MyPageView, self).get_context_data(**kwargs)
        context['site_name'] = 'MyPage'
        return context
