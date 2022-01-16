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

# creates get and post 
class personList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# creates ,update ,deleate ,patch
class personDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
