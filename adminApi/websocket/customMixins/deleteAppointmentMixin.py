from typing import Any, Tuple, Dict, OrderedDict
from rest_framework import status

from websocket.models.appointment import Appointment

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class DeleteAppointmentMixin:

    @action()
    def deleteAppointment(self, **kwargs) -> Tuple[None, int]:
        id = kwargs['id']
        instance = self.get_appointment(id)
        instance.delete()
        return "success", status.HTTP_204_NO_CONTENT


    def get_appointment(self, id, **kwargs):
        try:
            return Appointment.objects.get(id=id)
        except Appointment.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND