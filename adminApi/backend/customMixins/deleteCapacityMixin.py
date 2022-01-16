from typing import Any, Tuple, Dict, OrderedDict
from rest_framework import status

from backend.models.capacity import Capacity

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class DeleteCapacityMixin:
    """Delete model mixin"""

    @action()
    def deleteCapacity(self, **kwargs) -> Tuple[None, int]:

        '''
        sample JSON do delete capacity with pk 1 via socket

        {
            "action" : "deleteCapacity",
            "request_id" : 123,
            "pk" : "1"		
        }
        '''
        
        pk = kwargs['pk']
        instance = self.get_capacity(pk)
        instance.delete()
        return "success", status.HTTP_204_NO_CONTENT

    def deleteAllCapacities(self, **kwargs) -> Tuple[None, int]:
        Capacity.objects.all().delete()
        return "success", status.HTTP_204_NO_CONTENT

    def get_capacity(self, pk, **kwargs):
        try:
            return Capacity.objects.get(pk=pk)
        except Capacity.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND