from collections import defaultdict
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from rest_framework import generics, serializers, viewsets
from rest_framework.views import APIView
#from rest_framework.decorators import Response
from backend.api.serializers import faqQuestionSerializer ,appointmentSerializer, donationQuestionSerializer, requestIDSerializer, requestSerializer, personSerializer, capacitySerializer
from .models.appointment import appointment
from .models.donationQuestion import donationQuestion
from .models.request import request
from .models.person import person
from .models.capacity import capacity
from .models.faqQuestion import faqQuestion
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
        reserved = appointment.objects.filter(start__date = date_str)                     # getting all reserved appointments of a certain day 
        capacities = capacity.objects.filter(start__date = date_str)                      # getting all capacities of a certain day 
        
        for element in capacities:                                                        # going over all capacities of the day
            startOfN = capacity.get_start(element).time()
            durationOfN = capacity.get_duration(element)                                  # how long is the capacity
            slotsOfN = capacity.get_slots(element)                                        # how many slots are in the capacity
            
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
    serializer_class = requestIDSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = appointment.objects.filter(id=id)
            
        return queryset


class appointmentCreate(generics.ListCreateAPIView): 
    serializer_class = appointmentSerializer

    def get_queryset(self):
        queryset = appointment.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(id=id)
            
        return queryset
    
    def post(self, request, format=None):
        serializer = appointmentSerializer(data = request.data)
#                                                                                           appointment length should be exchangeable Verwaltungsoberfläche                                                          
        appointmentLength = int(60)                                                       # in minutes                   
#                                                                                           one slot is one hour, in minutes
        start = parse_datetime(str(request.data.get('start')))                            # access date via request 
        start_date = start.date()
        start_time = start.time()
        reserved = appointment.objects.filter(start = start)                              # geting all reserved appointments of a certain day 
        capacities = capacity.objects.filter(start__date = start_date)                    # geting all capacities of a certain day 

        for element in capacities:                                                        # going over all capacities of the day
            startOfN = capacity.get_start(element).time()                                 # when does the capacity start 
            durationOfN = capacity.get_duration(element)                                  # how long is the capacity
            slotsOfN = capacity.get_slots(element)                                        # how many slots are there in the capacity

            endCap = addTime(startOfN, timedelta(minutes=durationOfN))
            endApp = addTime(start_time, timedelta(minutes=appointmentLength))
            
            if (startOfN <= start_time) and \
                endCap >= endApp and \
                slotsOfN > len(reserved.filter(start__time = start_time)) and\
                serializer.is_valid() :
                    
                instance = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        error = {'error': 'HTTP_400_BAD_REQUEST' , 'message':'du bist ein schlingel'}
        return Response(data=json.loads(json.dumps(error)) , status = status.HTTP_400_BAD_REQUEST )
                    
            
            

    



class donationQuestionList(generics.ListCreateAPIView):
    queryset = donationQuestion.objects.all()
    serializer_class = donationQuestionSerializer

class faqQuestionsList(generics.ListCreateAPIView):
    queryset = faqQuestion.objects.all()
    serializer_class = faqQuestionSerializer

'''def index(request):
    return render(request, 'backend/index.html')'''

'''
# creates ,update ,deleate ,patch
class appointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = appointment.objects.all()
    serializer_class = appointmentSerializer
'''


# creates get and post 
class requestList(generics.ListCreateAPIView):
    queryset = request.objects.all()
    serializer_class = requestSerializer

# creates ,update ,deleate ,patch
class requestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = appointment.objects.all()
    serializer_class = requestSerializer 


# creates get and post 
class personList(generics.ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = personSerializer

# creates ,update ,deleate ,patch
class personDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = person.objects.all()
    serializer_class = personSerializer 


# creates get and post 
class capacityList(generics.ListCreateAPIView):
    queryset = capacity.objects.all()
    serializer_class = capacitySerializer

# creates ,update ,deleate ,patch
class capacityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = capacity.objects.all()
    serializer_class = capacitySerializer