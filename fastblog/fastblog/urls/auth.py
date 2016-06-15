from django.conf.urls import url

from fastblog.views.auth import *


urlpatterns = [
    url(r'^signup/$', SignupView.as_view(), name='signup'),

]
