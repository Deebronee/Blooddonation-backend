from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action

from backend.api.serializers import appointmentsSerializer
from backend.models.appointments import appointments

class appointmentsConsumer(GenericAsyncAPIConsumer):
    queryset = appointments.objects.all()
    serializer_class = appointmentsSerializer

    @model_observer(appointments)
    async def appointments_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @appointments_activity.serializer
    def appointments_activity(self, instance: appointments, action, **kwargs):
        return appointmentsSerializer(instance).data

    @action()
    async def subscribe_to_appointment_activity(self, **kwargs):
        await self.appointments_activity.subscribe()