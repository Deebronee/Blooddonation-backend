from typing import Any, Tuple, Dict, OrderedDict
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict
from websocket.serializers import CapacitySerializer

from websocket.models.capacity import Capacity

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class CreateCapacitiesMixin:

    @action()
    def createCapacities(self, data: dict, **kwargs) -> Tuple[ReturnDict, int]:
        
        Capacity.objects.all().delete()
        serializer = CapacitySerializer(data=data, many = True)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer, **kwargs)
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED

    def perform_create(self, serializer, **kwargs):
        serializer.save()

