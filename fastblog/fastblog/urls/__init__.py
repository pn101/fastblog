from django.conf.urls import url, include
from django.contrib import admin

from fastblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
