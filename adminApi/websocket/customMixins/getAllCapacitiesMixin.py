from typing import Any, Tuple, Dict, OrderedDict
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnList
from websocket.serializers import CapacitySerializer

from websocket.models.capacity import Capacity

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class GetAllCapacitiesMixin:
    
    @action()
    def getAllCapacities(self, **kwargs) -> Tuple[ReturnList, int]:

        queryset = Capacity.objects.all()
        serializer = CapacitySerializer(
            instance=queryset, many=True
        )
        return serializer.data, status.HTTP_200_OK