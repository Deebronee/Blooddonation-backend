from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action
from .customMixins.getAllCapacitiesMixin import GetAllCapacitiesMixin
from .customMixins.getAllAppointmentsMixin import GetAllAppointmentsMixin
from backend.rest_api.serializers import AppointmentSerializer
from backend.models.appointment import Appointment


# Get list of appointments, patch appointments, create appointments via JSON
class WebsocketConsumer(GenericAsyncAPIConsumer, GetAllCapacitiesMixin, GetAllAppointmentsMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @model_observer(Appointment)
    async def appointments_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @appointments_activity.serializer
    def appointments_activity(self, instance: Appointment, action, **kwargs):
        return AppointmentSerializer(instance).data

    @action()
    async def subscribe_to_appointment_activity(self, **kwargs):
        await self.appointments_activity.subscribe()

   