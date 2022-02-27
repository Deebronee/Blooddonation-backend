from collections import defaultdict
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from rest_framework import generics, serializers, viewsets
from rest_framework.views import APIView
#from rest_framework.decorators import Response
from rest_api.rest_api.serializers import FaqQuestionSerializer ,AppointmentSerializer, DonationQuestionSerializer, RequestIDSerializer, RequestSerializer, PersonSerializer, CapacitySerializer
from rest_api.models.appointment import Appointment
from rest_api.models.donationQuestion import DonationQuestion
from rest_api.models.request import Request
from rest_api.models.person import Person
from rest_api.models.capacity import Capacity
from rest_api.models.faqQuestion import FaqQuestion
from rest_framework.response import Response
import json
from datetime import time, timedelta, datetime, date
from django.utils.dateparse import parse_date, parse_datetime, parse_time
from rest_framework import status
import math


def addTime(setTime, timeToAdd):
        return ((datetime.combine(date.today(), setTime) + timeToAdd).time()) 


# request handler
# Create your views here.
# request --> response

# creates get and post 
class freeAppointmentsView(APIView):

    def get(self, request, format=None):
        free_List = []         
#                                                                                           appointment length should be exchangeable Verwaltungsoberfläche                                                          
        appointmentLength = int(60)                                                       # in minutes                     
#                                                                                           one slot is one hour, in minutes
        date_str = parse_date(str(request.GET.get('date')))                               # access date via request 
        reserved = Appointment.objects.filter(start__date = date_str)                     # getting all reserved appointments of a certain day 
        capacities = Capacity.objects.filter(start__date = date_str)                      # getting all capacities of a certain day 
        
        for element in capacities:                                                        # going over all capacities of the day
            startOfN = Capacity.get_start(element).time()
            durationOfN = Capacity.get_duration(element)                                  # how long is the capacity
            slotsOfN = Capacity.get_slots(element)                                        # how many slots are in the capacity
            
            for i in range(1380 // appointmentLength) :                                   # for-loop iterates through all possible appointments of a day
                j = i*appointmentLength
                time_j = time(math.floor(j/60),j%60,00)
                endCap = addTime(startOfN, timedelta(minutes=durationOfN))
                endApp = addTime(time_j, timedelta(minutes=appointmentLength))

                if startOfN <= time_j and (endCap >= endApp):

                    availableAppointments = slotsOfN - len(reserved.filter(start__time=time_j))

                    for _ in range(availableAppointments):    
                        dt = datetime.combine(date_str, time_j)
                        data = {}
                        data['start'] = dt
                        data['duration'] = appointmentLength
                        
                        free_List.append(data)                                            # f the amount of reserved slots is lower than the amount of overall slots then 

        return Response(free_List) 

class appointmentStatusView(generics.ListCreateAPIView):
    serializer_class = RequestIDSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id')
        appointment = Appointment.objects.filter(id=id)
        
        return appointment


class appointmentCreate(generics.ListCreateAPIView): 
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(id=id)
            
        return queryset
    
    def post(self, request):
        data = request.data.copy()
        data.__setitem__('request.created', datetime.now())
        data.__setitem__('request.status', 'requested')
        serializer = AppointmentSerializer(data=data)
      
#                                                                                           appointment length should be exchangeable Verwaltungsoberfläche                                                          
        appointmentLength = int(60)                                                       # in minutes                   
#                                                                                           one slot is one hour, in minutes
        start = parse_datetime(str(request.data.get('start')))                            # access date via request 
        start_date = start.date()
        start_time = start.time()
        reserved = Appointment.objects.filter(start = start)                              # geting all reserved appointments of a certain day 
        capacities = Capacity.objects.filter(start__date = start_date)                    # geting all capacities of a certain day 

        for element in capacities:                                                        # going over all capacities of the day
            startOfN = Capacity.get_start(element).time()                                 # when does the capacity start 
            durationOfN = Capacity.get_duration(element)                                  # how long is the capacity
            slotsOfN = Capacity.get_slots(element)                                        # how many slots are there in the capacity

            endCap = addTime(startOfN, timedelta(minutes=durationOfN))
            endApp = addTime(start_time, timedelta(minutes=appointmentLength))
            
            if (startOfN <= start_time) and \
                endCap >= endApp and \
                slotsOfN > len(reserved.filter(start__time = start_time)) and\
                serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        error = {'error': 'HTTP_400_BAD_REQUEST' , 'message':'du bist ein schlingel'}
        return Response(data=json.loads(json.dumps(error)) , status = status.HTTP_400_BAD_REQUEST)
                    

class appointmentCancel(APIView):

    def get(self, request):
        
        id = self.request.query_params.get('id')
        appointment = Appointment.objects.filter(id=id).delete()

        return Response("successful") 