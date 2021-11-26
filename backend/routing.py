from django.urls import re_path

from backend import consumers

websocket_urlpatterns = [
    re_path(r'ws/backend/$', consumers.ChatConsumer.as_asgi()),
]