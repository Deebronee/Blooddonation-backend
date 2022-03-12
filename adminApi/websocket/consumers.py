from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from websocket.customMixins.createCapacitiesMixin import CreateCapacitiesMixin
from websocket.customMixins.deleteAppointmentMixin import DeleteAppointmentMixin
from websocket.customMixins.createAppointmentMixin import CreateAppointmentMixin
from websocket.customMixins.getAllCapacitiesMixin import GetAllCapacitiesMixin
from websocket.customMixins.getAllAppointmentsMixin import GetAllAppointmentsMixin
from websocket.customMixins.createCapacitiesMixin import CreateCapacitiesMixin
from websocket.customMixins.createFaqQuestionsMixin import CreateFaqQuestionsMixin
from websocket.customMixins.createDonationQuestionsMixin import CreateDonationQuestionsMixin
from websocket.customMixins.getAllFaqQuestionsMixin import GetAllFaqQuestionsMixin
from websocket.customMixins.getAllDonationQuestionsMixin import GetAllDonationQuestionsMixin
from websocket.customMixins.newAppointmentsMixin import NewAppointmentsMixin
from websocket.customMixins.getStatisticMixin import GetStatisticMixin
from websocket.serializers import AppointmentSerializer
from websocket.models.appointment import Appointment
#import asyncio
#import psycopg2
#import os


# Get list of appointments, patch appointments, create appointments via JSON
class WebsocketConsumer(GenericAsyncAPIConsumer, 
                        GetAllCapacitiesMixin, 
                        GetAllAppointmentsMixin, 
                        CreateAppointmentMixin, 
                        CreateCapacitiesMixin, 
                        CreateFaqQuestionsMixin,
                        CreateDonationQuestionsMixin,
                        DeleteAppointmentMixin,
                        GetAllFaqQuestionsMixin,
                        GetAllDonationQuestionsMixin,
                        NewAppointmentsMixin,
                        GetStatisticMixin
                        ):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
