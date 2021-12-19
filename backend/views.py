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
        # appointment length should be exchangeable Verwaltungsoberfläche                                                          
        appointmentLength = int(60)                                             # in minuten                     
        # access date via request                                                         # one slot is one hour, in minutes
        date_str = parse_date(str(request.GET.get('date')))
        reserved = appointment.objects.filter(start__date = date_str)                               # geting all reserved appointments of a certan day 
        capacities = capacity.objects.filter(start__date = date_str)                                      # geting all pacacatys of a certan ay 
        for n in range(len(capacities)):                                                         # going over all capacatys of the day
            startOfN = capacity.get_start(capacities[n]).time()
                          # when does capacaty n start 
            durationOfN = capacity.get_duration(capacities[n])                           # how long is capacaty n
            slotsOfN = capacity.get_slots(capacities[n])                                  # how many slots are there in the capacaty
            for i in range(1380 // appointmentLength) :                                         # a day has 1440 minutes 
                j = i*appointmentLength
                time_j = time(math.floor(j/60),j%60,00)                                          # devide i by the appointmentlength to get the right slot of the day 
                #if startOfN_datetime <= time_j and (startOfN_datetime + timedelta(minutes=durationOfN)) <= (time_j + timedelta(minutes=appointmentLength)) :  # checking if the time of the day is after the start of the timeslot and bevor the end of the timeslot - one timesolt
                endCap = addTime(startOfN, timedelta(minutes=durationOfN))
                endApp = addTime(time_j, timedelta(minutes=appointmentLength))
                if startOfN <= time_j and (endCap >= endApp):
                    for k in range((slotsOfN - len(reserved.filter(start__time=time_j)))):    
                        
                        dt = datetime.combine(date_str, time_j)
                        data = {}
                        data['start'] = dt
                        data['duration'] = appointmentLength
                        
                        free_List.append(data)                                           # of the ammount of reserved slots is lower then the ammount of overall slots than 

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
        # appointment length should be exchangeable Verwaltungsoberfläche                                                          
        appointmentLength = int(60)                                             # in minuten                     
        # access date via request                                                         # one slot is one hour, in minutes
        start = parse_datetime(str(request.data.get('start')))
        start_date = start.date()
        start_time = start.time()
        reserved = appointment.objects.filter(start = start)                             # geting all reserved appointments of a certan day 
        capacities = capacity.objects.filter(start__date = start_date)                   # geting all pacacatys of a certan ay 
        for n in range(len(capacities)):                                                 # going over all capacatys of the day
            startOfN = capacity.get_start(capacities[n]).time()                          # when does capacaty n start 
            durationOfN = capacity.get_duration(capacities[n])                           # how long is capacaty n
            slotsOfN = capacity.get_slots(capacities[n])                                 # how many slots are there in the capacaty
            
            endCap = addTime(startOfN, timedelta(minutes=durationOfN))
            endApp = addTime(start_time, timedelta(minutes=appointmentLength))
            
            if (startOfN <= start_time) and \
                endCap >= endApp and \
                slotsOfN - len(reserved.filter(start__time = start_time)) and\
                serializer.is_valid() :
                    
                instance = serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        error = {'error': 400 , 'message':'du bist ein schlingel'}
        return Response( data=json.dumps(error) , status = status.HTTP_400_BAD_REQUEST )
                    
            
            

    



class donationQuestionList(generics.ListCreateAPIView):
    queryset = donationQuestion.objects.all()
    serializer_class = donationQuestionSerializer

class faqQuestionsList(generics.ListCreateAPIView):
    queryset = faqQuestion.objects.all()
    serializer_class = faqQuestionSerializer

'''def index(request):
    return render(request, 'backend/index.html')'''

'''# creates ,update ,deleate ,patch
class appointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = appointment.objects.all()
    serializer_class = appointmentSerializer '''


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