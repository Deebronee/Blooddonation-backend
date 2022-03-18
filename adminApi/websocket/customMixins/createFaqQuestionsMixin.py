from typing import Any, Tuple, Dict, OrderedDict
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict
from websocket.serializers import FaqQuestionTranslationSerializer, FaqQuestionSerializer


from websocket.models.faqQuestionTranslation import FaqQuestionTranslation
from websocket.models.faqQuestion import FaqQuestion

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class CreateFaqQuestionsMixin:

    @action()
    def createFaqQuestions(self, data: dict, **kwargs) -> Tuple[ReturnDict, int]:
        
        FaqQuestionTranslation.objects.all().delete()
        FaqQuestion.objects.all().delete()

        translationSerializer = FaqQuestionTranslationSerializer(data=data["translationData"], many = True)
        questionSerializer = FaqQuestionSerializer(data = data["questionData"], many = True)
        translationSerializer.is_valid(raise_exception=True)
        questionSerializer.is_valid(raise_exception=True)

        #self.perform_create(serializer, **kwargs)
        translationSerializer.save()
        questionSerializer.save()

        response = {
            "faqQuestions" : questionSerializer.data,
            "faqQuestionTranslations": translationSerializer.data
        }
        return response, status.HTTP_201_CREATED

    def perform_create(self, serializer, **kwargs):
        serializer.save()


