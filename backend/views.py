from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from backend.api.serializers import blood_donation_appointmentsSerializer, kill_questionsSerializer
from .models import blood_donation_appointments, kill_questions
# request handler
# Create your views here.
# request --> response
'''
class ApintmentsViewSet(viewsets.ModelViewSet):
    queryset = blood_donation_free_appointments.objects.all()
    serializer_class = blood_donation_free_appointmentsSerializer
'''

# creates get and post 
class blood_donation_free_appointmentsList(generics.ListCreateAPIView): 
    queryset = blood_donation_appointments.objects.filter(reserved = False , assigned = False) # Checking for all that are not reserved and not assigned so that are free
    serializer_class = blood_donation_appointmentsSerializer
    
class blood_donation_reserved_appointmentsList(generics.ListCreateAPIView): 
    queryset = blood_donation_appointments.objects.filter(reserved = True , assigned = False) # Checking for all that are reserved and not assigned so that are ready to be accepted
    serializer_class = blood_donation_appointmentsSerializer
    
class blood_donation_assigned_appointmentsList(generics.ListCreateAPIView): 
    queryset = blood_donation_appointments.objects.filter(reserved = True , assigned = True) # Checking for all that are reserved and assigned so that are accepted
    serializer_class = blood_donation_appointmentsSerializer


# creates ,update ,deleate ,patch
class blood_donation_appointmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = blood_donation_appointments.objects.all()
    serializer_class = blood_donation_appointmentsSerializer 


class kill_questionsList(generics.ListCreateAPIView): 
    queryset = kill_questions.objects.all()
    serializer_class = kill_questionsSerializer