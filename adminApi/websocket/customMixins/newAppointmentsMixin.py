from typing import Any, Tuple, Dict, OrderedDict
from django.test import TransactionTestCase
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from websocket.serializers import AppointmentSerializer
from django.db.models import Q

from websocket.models.appointment import Appointment
import sched, time
from .decorators import action
from djangochannelsrestframework.settings import api_settings


class NewAppointmentsMixin:
    
    @action()
    def newAppointments(self, data : dict, **kwargs) -> Tuple[ReturnList, int]:

        id = data['id']
        lastApp = Appointment.objects.last()
        lastAppID = lastApp.id
        newAppointments = []

        for x in range(lastAppID - id):
            myID = id + x + 1
            appointment = Appointment.objects.get(id=myID)
            print(appointment.request.status)
            if appointment.request.status != "accepted":
                serialized = AppointmentSerializer(appointment).data
                newAppointments.append(serialized)
            
        return newAppointments, status.HTTP_200_OK
