from typing import Any, Tuple, Dict, Optional, OrderedDict, Union
from django.db.models import query
from djangochannelsrestframework.observer.model_observer import Action
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from backend.api.serializers import appointmentSerializer

from backend.models.appointment import appointment

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class GetAllAppointmentsMixin:
    """List model mixin"""
    @action()
    def getAllAppointments(self, **kwargs) -> Tuple[ReturnList, int]:
        """List action.
        Returns:
            Tuple with the list of serializer data and the status code.
        Examples:
            .. code-block:: python
                #! consumers.py
                from .models import User
                from .serializers import UserSerializer
                from djangochannelsrestframework import permissions
                from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
                from djangochannelsrestframework.mixins import ListModelMixin
                class LiveConsumer(ListModelMixin, GenericAsyncAPIConsumer):
                    queryset = User.objects.all()
                    serializer_class = UserSerializer
                    permission_classes = (permissions.AllowAny,)
            .. code-block:: python
                #! routing.py
                from django.urls import re_path
                from .consumers import LiveConsumer
                websocket_urlpatterns = [
                    re_path(r'^ws/$', LiveConsumer.as_asgi()),
                ]
            .. code-block:: javascript
                // html
                const ws = new WebSocket("ws://localhost:8000/ws/")
                ws.send(JSON.stringify({
                    action: "list",
                    request_id: new Date().getTime(),
                }))
                /* The response will be something like this.
                {
                    "action": "list",
                    "errors": [],
                    "response_status": 200,
                    "request_id": 1500000,
                    "data": [
                        {"email": "42@example.com", "id": 1, "username": "test1"},
                        {"email": "45@example.com", "id": 2, "username": "test2"},
                    ],
                }
                */
        """
        queryset = appointment.objects.all()
        serializer = appointmentSerializer(
            instance=queryset, many=True
        )
        return serializer.data, status.HTTP_200_OK