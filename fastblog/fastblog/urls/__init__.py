from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from fastblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
