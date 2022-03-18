from typing import Any, Tuple, Dict, OrderedDict
from django.test import TransactionTestCase
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from websocket.serializers import AppointmentSerializer
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from websocket.models.appointment import Appointment
import sched, time
from .decorators import action
from djangochannelsrestframework.settings import api_settings


class NewAppointmentsMixin:
    
    @action()
    def newAppointments(self, data : dict, **kwargs) -> Tuple[ReturnList, int]:

        if not "id" in data:
            return [], status.HTTP_200_OK
        
        if Appointment.objects.count() == 0:
            return [], status.HTTP_200_OK


        id = data['id']
        lastApp = Appointment.objects.last()
        lastAppID = lastApp.id

        if id > lastAppID:
            return [], status.HTTP_200_OK

        newAppointments = []
    

        for x in range(lastAppID - id):
            myID = id + x + 1
            try:
                appointment = Appointment.objects.get(id=myID)
                if appointment.request.status != "accepted":
                    serialized = AppointmentSerializer(appointment).data
                    newAppointments.append(serialized)
            except Appointment.DoesNotExist:
                continue

            
        return newAppointments, status.HTTP_200_OK
