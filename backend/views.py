from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from backend.api.serializers import appointmentSerializer, donationQuestionSerializer, requestSerializer, personSerializer, capacitySerializer
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
    serializer_class = appointmentSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = appointment.objects.all()
        start = self.request.query_params.get('start')
        if start is not None:
            queryset = queryset.filter(appointment__start=start)
        return queryset
    
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