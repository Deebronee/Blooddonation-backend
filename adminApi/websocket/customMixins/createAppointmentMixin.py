from datetime import timedelta, datetime, date
import json
from typing import Tuple
from django.db.models import query
from django.http.request import QueryDict
from django.utils.dateparse import parse_datetime
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict
from websocket.models.capacity import Capacity
from websocket.serializers import AppointmentSerializer
from websocket.adminStatisticFunctions import acceptedRequests, rejectedRequests, aged18to27, aged28to37, aged38to47, aged48to57, aged58to68, numberOfFirstTimeDonations


from websocket.models.appointment import Appointment

from .decorators import action
from djangochannelsrestframework.settings import api_settings

def addTime(setTime, timeToAdd):
    return ((datetime.combine(date.today(), setTime) + timeToAdd).time()) 

def calcAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

class CreateAppointmentMixin:

    @action()
    def createAppointment(self, data: QueryDict, **kwargs) -> Tuple[ReturnDict, int]:

        '''
        sample JSON to create appointment

        {
	        "action" : "createAppointment",
            "request_id" : 123,
	        "data" : 
		        {
        		        "start": "2022-01-11T12:00:00Z",
        		        "duration": 60,
        		        "person": 
			                {
           			            "name": "Websocket Tester",
            			        "birthday": null,
            			        "gender": ""
        		            }
		    }
        }
        '''
        dic = {'created': datetime.now(), 'status': 'pending'}
        
        data['request'] = dic
        serializer = AppointmentSerializer(data=data)
#                                                                                           appointment length should be exchangeable Verwaltungsoberfläche                                                          
        appointmentLength = int(15)                                                       # in minutes                   
#                                                                                           one slot is one hour, in minutes
        start = parse_datetime(str(data['start']))                            # access date via request 
        start_date = start.date()
        start_time = start.time()
        reserved = Appointment.objects.filter(start = start)                              # geting all reserved appointments of a certain day 
        capacities = Capacity.objects.filter(start__date = start_date)                    # geting all capacities of a certain day 

        for element in capacities:                                                        # going over all capacities of the day
            startOfN = Capacity.get_start(element).time()                              # when does the capacity start 
            durationOfN = Capacity.get_duration(element)                                  # how long is the capacity
            slotsOfN = Capacity.get_slots(element)                                        # how many slots are there in the capacity

            endCap = addTime(startOfN, timedelta(minutes=durationOfN))
            endApp = addTime(start_time, timedelta(minutes=appointmentLength))
            
            serializer.is_valid(raise_exception=True)

            if (startOfN <= start_time) and \
                endCap >= endApp and \
                slotsOfN > len(reserved.filter(start__time = start_time)):
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return serializer.data, status.HTTP_201_CREATED

        #print(serializer.errors)
        error = {'error': 'HTTP_400_BAD_REQUEST' , 'message':'du bist ein schlingel'}
        return json.loads(json.dumps(error)) , status.HTTP_400_BAD_REQUEST
    
    
    def perform_create(self, serializer, **kwargs):
        serializer.save()
    

    # TODO patch request via websocket
    @action()
    def updateAppointment(self, data: QueryDict, **kwargs) -> Tuple[ReturnDict, int]:

        '''
        sample JSON to update appointment

        {
	        "action" : "updateAppointment",
            "request_id" : 123,
            "id" : 1,
	        "data" : 
		        {
        		    "request" : 
                        {
                            "created" : "2024-01-01T00:00:00",
                            "status" : "confirmed"
                        }
		        }
        }
        '''

        instance = Appointment.objects.get(id= kwargs['id'])
        serializer = AppointmentSerializer(
            instance=instance, data=data, partial=True
        )
        serializer.is_valid(raise_exception=True)

        appointmentStatus = data['request']['status']
        birthdate = instance.person.birthday
        age = calcAge(birthdate)
        firstTime = instance.person.firstDonation

        if appointmentStatus == "accepted":
            acceptedRequests()
            if 18 <= age <= 27:
                aged18to27()
            if 28 <= age <= 37:
                aged28to37()
            if 38 <= age <= 47:
                aged38to47()
            if 48 <= age <= 57:
                aged48to57()
            if 58 <= age <= 68:
                aged58to68()
            if firstTime:
                numberOfFirstTimeDonations()
        if appointmentStatus == "rejected":
            rejectedRequests()
        serializer.save()
        return serializer.data, status.HTTP_200_OK


    
