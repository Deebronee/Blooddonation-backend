from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/backend/appointment', consumers.appointmentsConsumer.as_asgi()),
    #re_path(r'ws/backend/request', consumers.requestsConsumer.as_asgi()),
    re_path(r'ws/backend/capacity', consumers.capacityConsumer.as_asgi())
]