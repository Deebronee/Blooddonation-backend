from rest_framework import generics
from backend.api.serializers import appointmentsSerializer
from backend.views import appointmentsDetail


class assigned_appointmentsList(generics.ListCreateAPIView): 
    queryset = appointmentsDetail.objects.filter(reserved = True , assigned = True) # Checking for all that are reserved and assigned so that are accepted
    serializer_class = appointmentsSerializer