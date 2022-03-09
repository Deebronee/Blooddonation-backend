from typing import Tuple
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnList
from websocket.serializers import StatisticSerializer
from websocket.models.statistic import Statistic
from .decorators import action

class GetStatisticMixin:

    @action()
    def getStatistic(self, **kwargs) -> Tuple[ReturnList, int]:
        queryset = Statistic.objects.all()
        serializer = StatisticSerializer(
            instance=queryset, many=True
        )
        return serializer.data, status.HTTP_200_OK