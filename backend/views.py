from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from backend.api.serializers import blood_donation_free_appointmentsSerializer
from .models import blood_donation_free_appointments
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
    queryset = blood_donation_free_appointments.objects.all()
    serializer_class = blood_donation_free_appointmentsSerializer

# creates ,update ,deleate ,patch
class blood_donation_free_appointmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = blood_donation_free_appointments.objects.all()
    serializer_class = blood_donation_free_appointmentsSerializer 
