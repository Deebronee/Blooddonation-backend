from django.shortcuts import render
from django.http import HttpResponse, response
from rest_framework import generics, serializers, viewsets
from rest_framework.views import APIView
#from rest_framework.decorators import Response
from backend.api.serializers import faqQuestionSerializer ,appointmentSerializer, donationQuestionSerializer, requestSerializer, personSerializer, capacitySerializer
from .models.appointment import appointment
from .models.donationQuestion import donationQuestion
from .models.request import request
from .models.person import person
from .models.capacity import capacity
from .models.faqQuestion import faqQuestion
from rest_framework.response import Response
import json
from datetime import time, timedelta
from django.utils.dateparse import parse_date


# request handler
# Create your views here.
# request --> response

# creates get and post 
class appointmentsList(APIView):
    def get(self, request, format=None):
        free_List = []                                                                      
        appointmentLength = int(60)                     
        # access date via request                                                         # one slot is one hour, in minutes
        date_str = str(request.GET.get('date'))
        reserved = appointment.objects.filter(date = parse_date(date_str))                               # geting all reserved appointments of a certan day 
        capacities = capacity.objects.filter(date = parse_date(date_str))                                      # geting all pacacatys of a certan ay 
        for n in range(len(capacities)):                                                         # going over all capacatys of the day
            startOfN = capacity.get_time(capacities[n])                                    # when does capacaty n start 
            durationOfN = capacity.get_duration(capacities[n])                           # how long is capacaty n
            slotsOfN = capacity.get_slots(capacities[n])                                  # how many slots are there in the capacaty
            for i in range(1440 // appointmentLength) :                                         # a day has 1440 minutes 
                j = i*appointmentLength
                time_j = time(j,00,00,000000)                                                   # devide i by the appointmentlength to get the right slot of the day 
                if startOfN <= time_j and (startOfN + timedelta(minutes=durationOfN)) <= (time_j + timedelta(minutes=appointmentLength)) :  # checking if the time of the day is after the start of the timeslot and bevor the end of the timeslot - one timesolt
                    for k in range((slotsOfN - len(reserved.filter(time=time_j)))):     
                                                                                       # of the ammount of reserved slots is lower then the ammount of overall slots than 
                        free_List.append('{"date": ' + date_str + ', '
                                        + '"time": ' + time_j + ', '
                                        + '"duration": ' + appointmentLength + '}')

        addComma = ', '.join(free_List)       # die daten typen sind noch nicht richtig aber habe es bis jetzt noch nicht richitg inbekommen
        addBrackets = "[" + addComma + "]"
        return Response(str(addBrackets))            # to string

'''
class appointmentsList(APIView):
    def get(self, request, date, format=None):
        free_List = []
        appointmentLength = 60                                                            # one slot is one hour, in minutes
        reserved = appointment.objects.filter(date = date)                                # geting all reserved appointments of a certan day 
        capacities = capacity.objects.filter(date = date)                                 # geting all pacacatys of a certan ay 
        for n in len(capacities):                                                         # going over all capacatys of the day
            startOfN = capacity.get_time(capacities[n])                                   # when does capacaty n start 
            durationOfN = capacity.get_duration(capacities[n])                            # how long is capacaty n
            slotsOfN = capacity.get_slots(capacities[n])                                  # how many slots are there in the capacaty
            for i in (1440 / appointmentLength) :                                         # a day has 1440 minutes 
                j = i*appointmentLength                                                   # devide i by the appointmentlength to get the right slot of the day 
                if startOfN >= j and (startOfN + durationOfN - appointmentLength ) < j :  # checking if the time of the day is after the start of the timeslot and bevor the end of the timeslot - one timesolt
                    if len(reserved.filter(time = j)) < slotsOfN:                         # of the ammount of reserved slots is lower then the ammount of overall slots than 
                        free_List.append(j)
                    # die daten typen sind noch nicht richtig aber habe es bis jetzt noch nicht richitg inbekommen
        serializer = appointmentSerializer(free_List)
        return Response(serializer.data)
'''


class free_appointmentList(generics.ListCreateAPIView): 
    queryset = appointment.objects.all() # Checking for all that are not reserved and not assigned so that are free
    serializer_class = appointmentSerializer

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


'''# creates get and post 
class requestList(generics.ListCreateAPIView):
    queryset = request.objects.all()
    serializer_class = requestSerializer'''

'''# creates ,update ,deleate ,patch
class requestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = appointment.objects.all()
    serializer_class = requestSerializer '''


'''# creates get and post 
class personList(generics.ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = personSerializer'''

'''# creates ,update ,deleate ,patch
class personDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = person.objects.all()
    serializer_class = personSerializer '''


# creates get and post 
class capacityList(generics.ListCreateAPIView):
    queryset = capacity.objects.all()
    serializer_class = capacitySerializer

# creates ,update ,deleate ,patch
class capacityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = capacity.objects.all()
    serializer_class = capacitySerializer