from django.conf.urls import url

from fastblog.views.posts import *


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', PostEditView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete'),

    url(r'^(?P<pk>\d+)/comments/create/$', PostCommentCreateView.as_view(), name='postcommentcreate'),
    url(r'^(?P<pk>\d+)/comments/(?P<comment_id>\d+)/edit/$', PostCommentEditView.as_view(), name='postcommentedit'),

]
