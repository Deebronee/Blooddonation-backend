from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)

from typing import Any, Tuple, Dict, Optional, OrderedDict, Union
from .customMixins.getAllCapacitiesMixin import GetAllCapacitiesMixin
from .customMixins.getAllAppointmentsMixin import GetAllAppointmentsMixin


from rest_framework import status

from backend.api.serializers import appointmentSerializer, requestSerializer, capacitySerializer
from backend.models.appointment import appointment
from backend.models.request import request
from backend.models.capacity import capacity
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList



# Get list of appointments, patch appointments, create appointments via JSON
class appointmentsConsumer(GenericAsyncAPIConsumer, ListModelMixin, UpdateModelMixin, CreateModelMixin, DeleteModelMixin, PatchModelMixin, GetAllCapacitiesMixin, GetAllAppointmentsMixin):
    queryset = appointment.objects.all()
    serializer_class = appointmentSerializer

    @model_observer(appointment)
    async def appointments_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @appointments_activity.serializer
    def appointments_activity(self, instance: appointment, action, **kwargs):
        return appointmentSerializer(instance).data

    @action()
    async def subscribe_to_appointment_activity(self, **kwargs):
        await self.appointments_activity.subscribe()


'''
# Request Notifications
class requestsConsumer(GenericAsyncAPIConsumer):
    queryset = request.objects.all()
    serializer_class = requestSerializer

    @model_observer(request)
    async def request_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @request_activity.serializer
    def request_activity(self, instance: request, action, **kwargs):
        return requestSerializer(instance).data

    @action()
    async def subscribe_to_request_activity(self, **kwargs):
        await self.request_activity.subscribe()
'''


class capacityConsumer(GenericAsyncAPIConsumer, CreateModelMixin, DeleteModelMixin, UpdateModelMixin, GetAllCapacitiesMixin):
    queryset = capacity.objects.all()
    serializer_class = capacitySerializer

   