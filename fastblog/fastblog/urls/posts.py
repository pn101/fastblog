from django.conf.urls import url

from fastblog.views.posts import *


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PostDetailView.as_view(), name='detail'),

]
