from rest_framework import generics
from backend.api.serializers import appointmentSerializer
from backend.views import appointmentDetail


'''class assigned_appointmentsList(generics.ListCreateAPIView): 
    queryset = appointmentDetail.objects.filter(reserved = True , assigned = True) # Checking for all that are reserved and assigned so that are accepted
    serializer_class = appointmentSerializer'''