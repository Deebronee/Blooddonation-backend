from rest_framework import generics
from backend.api.serializers import kill_questionsSerializer


class kill_questionsList(generics.ListCreateAPIView): 
    queryset = kill_questionsSerializer.objects.all()
    serializer_class = kill_questionsSerializer