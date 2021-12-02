from rest_framework import generics
from backend.api.serializers import appointmentsSerializer
from backend.models.appointment import appointments
from backend.views import appointmentsDetail

'''
# post get
class free_appointmentsList(generics.ListCreateAPIView): 
    queryset = appointmentsDetail.objects.filter(reserved = False , assigned = False) # Checking for all that are not reserved and not assigned so that are free
    serializer_class = appointmentsSerializer

#     
class appointmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = appointments.objects.all()
    serializer_class = appointmentsSerializer'''