from typing import Any, Tuple, Dict, OrderedDict
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict
from backend.serializers import CapacitySerializer

from backend.models.capacity import Capacity

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class CreateCapacitiesMixin:
    """ Create model mixin."""

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

'''
{
	"action" : "createCapacities",
    "request_id" : 123,
	"data" : 
        [{	
            "start" : "2022-01-01T12:00:00",
            "duration" : 180,
            "slots" : 30
        },
        {	
            "start" : "2022-01-01T14:00:00",
            "duration" : 120,
            "slots" : 10
        }]
}
'''