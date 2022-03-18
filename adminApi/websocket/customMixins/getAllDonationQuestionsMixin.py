from typing import Any, Tuple, Dict, OrderedDict
from django.test import TransactionTestCase
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnList
from websocket.serializers import DonationQuestionSerializer, DonationQuestionTranslationSerializer

from websocket.models.donationQuestion import DonationQuestion
from websocket.models.donationQuestionTranslation import DonationQuestionTranslation

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class GetAllDonationQuestionsMixin:
    
    @action()
    def getAllDonationQuestions(self, **kwargs) -> Tuple[ReturnList, int]:

        donationQuestionQueryset = DonationQuestion.objects.all()
        donationQuestionSerializer = DonationQuestionSerializer(
            instance=donationQuestionQueryset, many=True
        )

        donationQuestionTranslationQueryset = DonationQuestionTranslation.objects.all()
        donationQuestionTranslationSerializer = DonationQuestionTranslationSerializer(
            instance=donationQuestionTranslationQueryset, many=True
        )

        content = {
            "donationQuestions" : donationQuestionSerializer.data,
            "donationQuestionTranslations": donationQuestionTranslationSerializer.data
        }

        return content, status.HTTP_200_OK