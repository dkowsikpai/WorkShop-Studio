from django.conf.urls import url
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home-chat-server'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)