from rest_framework import generics
from backend.api.serializers import appointmentsSerializer
from backend.views import appointmentsDetail


'''class reserved_appointmentsList(generics.ListCreateAPIView): 
    queryset = appointmentsDetail.objects.filter(reserved = True , assigned = False) # Checking for all that are reserved and not assigned so that are ready to be accepted
    serializer_class = appointmentsSerializer'''