from django.conf.urls import url

from bitly.views import *


urlpatterns = [
    url(r'^dashboard/$', BitLinkDashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/(?P<shorten_hash>\w+)/$', BitLinkDashboardDetailListView.as_view(), name='dashboarddetail'),
    url(r'^create/$', BitLinkCreateView.as_view(), name='create'),
    url(r'^(?P<shorten_hash>\w+)/$', BitLinkRedirectView.as_view(), name='redirect'),

]
