from typing import Any, Tuple, Dict, OrderedDict
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict
from websocket.serializers import DonationQuestionTranslationSerializer, DonationQuestionSerializer

from websocket.models.donationQuestionTranslation import DonationQuestionTranslation
from websocket.models.donationQuestion import DonationQuestion


from .decorators import action
from djangochannelsrestframework.settings import api_settings

class CreateDonationQuestionsMixin:

    @action()
    def createDonationQuestions(self, data: dict, **kwargs) -> Tuple[ReturnDict, int]:
        
        DonationQuestionTranslation.objects.all().delete()
        DonationQuestion.objects.all().delete()

        translationSerializer = DonationQuestionTranslationSerializer(data=data["translationData"], many = True)
        questionSerializer = DonationQuestionSerializer(data = data["questionData"], many = True)
        translationSerializer.is_valid(raise_exception=True)
        questionSerializer.is_valid(raise_exception=True)

        #self.perform_create(serializer, **kwargs)
        translationSerializer.save()
        questionSerializer.save()

        response = {
            "donationQuestions" : questionSerializer.data,
            "donationQuestionTranslations": translationSerializer.data
        }
        return response, status.HTTP_201_CREATED

    def perform_create(self, serializer, **kwargs):
        serializer.save()
