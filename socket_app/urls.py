from django.urls import path
from socket_app import views

urlpatterns = [
    path('anzeigen', views.anzeigen, name = 'anzeigen'),
]