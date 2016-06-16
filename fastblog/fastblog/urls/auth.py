from django.conf.urls import url

from fastblog.views.auth import *


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^mypage/$', MyPageView.as_view(), name='mypage'),
    url(r'^yourpage/(?P<user_name>\w+)/$', YourPageView.as_view(), name='yourpage'),

]
