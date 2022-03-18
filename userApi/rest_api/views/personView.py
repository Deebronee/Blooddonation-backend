from rest_framework import generics
from rest_api.rest_api.serializers import PersonSerializer
from rest_api.models.person import Person


# creates get and post 
class personList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# creates ,update ,deleate ,patch
class personDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
