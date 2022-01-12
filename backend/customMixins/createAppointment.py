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
from backend.models.capacity import Capacity
from backend.rest_api.serializers import AppointmentSerializer
from django.core.serializers.json import DjangoJSONEncoder
import io
from rest_framework.parsers import JSONParser


from backend.models.appointment import Appointment
from backend.views import addTime

from .decorators import action
from djangochannelsrestframework.settings import api_settings

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
        appointmentLength = int(60)                                                       # in minutes                   
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

        instance = self.get_object(data=data, **kwargs)

        serializer = AppointmentSerializer(
            instance=instance, data=data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        self.perform_patch(serializer, **kwargs)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return serializer.data, status.HTTP_200_OK

    def perform_patch(self, serializer, **kwargs):
        serializer.save()