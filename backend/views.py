from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from backend.api.serializers import appointmentSerializer, donationQuestionSerializer, requestSerializer
from .models.appointment import appointment
from .models.donationQuestion import donationQuestion
from .models.request import request
from .models.person import person
from .models.capacity import capacity

# request handler
# Create your views here.
# request --> response
'''
class ApintmentsViewSet(viewsets.ModelViewSet):
    queryset = free_appointments.objects.all()
    serializer_class = free_appointmentsSerializer
'''

# creates get and post 
class free_appointmentList(generics.ListCreateAPIView): 
    queryset = appointment.objects.all() # Checking for all that are not reserved and not assigned so that are free
    serializer_class = appointmentSerializer
    
# creates ,update ,deleate ,patch
class appointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = appointment.objects.all()
    serializer_class = appointmentSerializer 


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


class donationQuestion(generics.ListCreateAPIView):
    queryset = donationQuestion.objects.all()
    serializer_class = donationQuestionSerializer

def index(request):
    return render(request, 'backend/index.html')