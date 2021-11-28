from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from backend.api.serializers import appointmentsSerializer, kill_questionsSerializer
from .models.appointments import appointments
from .models.kill_questions import kill_questions

# request handler
# Create your views here.
# request --> response
'''
class ApintmentsViewSet(viewsets.ModelViewSet):
    queryset = free_appointments.objects.all()
    serializer_class = free_appointmentsSerializer
'''

# creates get and post 
class free_appointmentsList(generics.ListCreateAPIView): 
    queryset = appointments.objects.filter(reserved = False , assigned = False) # Checking for all that are not reserved and not assigned so that are free
    serializer_class = appointmentsSerializer
    
class reserved_appointmentsList(generics.ListCreateAPIView): 
    queryset = appointments.objects.filter(reserved = True , assigned = False) # Checking for all that are reserved and not assigned so that are ready to be accepted
    serializer_class = appointmentsSerializer
    
class assigned_appointmentsList(generics.ListCreateAPIView): 
    queryset = appointments.objects.filter(reserved = True , assigned = True) # Checking for all that are reserved and  assigned so that are accepted
    serializer_class = appointmentsSerializer

# creates ,update ,deleate ,patch
class appointmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = appointments.objects.all()
    serializer_class = appointmentsSerializer 


class kill_questionsList(generics.ListCreateAPIView):
    queryset = kill_questions.objects.all()
    serializer_class = kill_questionsSerializer

def index(request):
    return render(request, 'backend/index.html')

