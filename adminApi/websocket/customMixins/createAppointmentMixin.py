from datetime import time, timedelta, datetime, date
import json
from typing import Any, Tuple, Dict, Optional, OrderedDict, Union
from django.db.models import query
from django.http.request import QueryDict
from django.utils.dateparse import parse_datetime
from djangochannelsrestframework.observer.model_observer import Action
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from rest_framework import response, status
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from websocket.models.capacity import Capacity
from websocket.serializers import AppointmentSerializer
from django.core.serializers.json import DjangoJSONEncoder
import io
from rest_framework.parsers import JSONParser
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
        
        #data.__setitem__('request.created', datetime.now())
        #data.__setitem__('request.status', 'pending')
        data['request'] = dic
        #print(data)
        serializer = AppointmentSerializer(data=data)
        #serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer, **kwargs)
        #return serializer.data, status.HTTP_201_CREATED
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
        #print(appointmentStatus)
        #print(instance.person.birthday)
        birthdate = instance.person.birthday
        #print(birthdate)

        age = calcAge(birthdate)
        #print(age)
        #print(instance)
        firstTime = instance.person.firstDonation
        #print(firstTime)
        #age = instance['person']['age']
        #print(age)

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


    
