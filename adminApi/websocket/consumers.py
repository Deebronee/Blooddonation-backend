from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action

from websocket.customMixins.createCapacitiesMixin import CreateCapacitiesMixin
from websocket.customMixins.deleteAppointmentMixin import DeleteAppointmentMixin
from websocket.customMixins.createAppointmentMixin import CreateAppointmentMixin
from websocket.customMixins.getAllCapacitiesMixin import GetAllCapacitiesMixin
from websocket.customMixins.getAllAppointmentsMixin import GetAllAppointmentsMixin
from websocket.customMixins.deleteCapacityMixin import DeleteCapacityMixin
from websocket.customMixins.createCapacitiesMixin import CreateCapacitiesMixin
from websocket.customMixins.createFaqQuestionsMixin import CreateFaqQuestionsMixin
from websocket.customMixins.createDonationQuestionsMixin import CreateDonationQuestionsMixin

from websocket.serializers import AppointmentSerializer
from websocket.models.appointment import Appointment


# Get list of appointments, patch appointments, create appointments via JSON
class WebsocketConsumer(GenericAsyncAPIConsumer, 
                        GetAllCapacitiesMixin, 
                        GetAllAppointmentsMixin, 
                        CreateAppointmentMixin, 
                        DeleteCapacityMixin, 
                        CreateCapacitiesMixin, 
                        CreateFaqQuestionsMixin,
                        CreateDonationQuestionsMixin,
                        DeleteAppointmentMixin):

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

   