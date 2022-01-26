from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'websocket', consumers.WebsocketConsumer.as_asgi())
]