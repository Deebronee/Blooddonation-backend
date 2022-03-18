from typing import Any, Tuple, Dict, OrderedDict
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnList
from websocket.serializers import AppointmentSerializer

from websocket.models.appointment import Appointment

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class GetAllAppointmentsMixin:

    @action()
    def getAllAppointments(self, **kwargs) -> Tuple[ReturnList, int]:

        queryset = Appointment.objects.all()
        serializer = AppointmentSerializer(
            instance=queryset, many=True
        )
        return serializer.data, status.HTTP_200_OK