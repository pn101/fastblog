from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from fastblog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^', include('fastblog.urls.auth', namespace='auth')),

    url(r'^fastblog/', include('fastblog.urls.posts', namespace='fastblog')),

    url(r'^bitly/', include('fastblog.urls.bitly', namespace='bitly')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
