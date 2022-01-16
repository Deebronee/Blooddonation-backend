from typing import Any, Tuple, Dict, Optional, OrderedDict, Union
from django.db.models import query
from djangochannelsrestframework.observer.model_observer import Action
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from backend.rest_api.serializers import AppointmentSerializer

from backend.models.appointment import Appointment

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class GetAllAppointmentsMixin:

    @action()
    def getAllAppointments(self, **kwargs) -> Tuple[ReturnList, int]:

        '''
        send JSON to get all appointments
        
        {
	        "action" : "getAllAppointments",
            "request_id" : 123
        }
        '''
        queryset = Appointment.objects.all()
        serializer = AppointmentSerializer(
            instance=queryset, many=True
        )
        return serializer.data, status.HTTP_200_OK