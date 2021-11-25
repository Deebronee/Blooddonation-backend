from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import WSConsumer
from channels.routing import ProtocolTypeRouter, URLRouter 

websocket_urlpatterns = [
    path('ws/anzeigen/', WSConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(URLRouter(websocket_urlpatterns)) 
})



