from typing import Any, Tuple, Dict, OrderedDict
from django.test import TransactionTestCase
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from websocket.serializers import FaqQuestionSerializer, FaqQuestionTranslationSerializer

from websocket.models.faqQuestion import FaqQuestion
from websocket.models.faqQuestionTranslation import FaqQuestionTranslation

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class GetAllFaqQuestionsMixin:
    
    @action()
    def getAllFaqQuestions(self, **kwargs) -> Tuple[ReturnList, int]:

        '''
        send JSON to get all capacities
        
        {
	        "action" : "getAllFaqQuestions",
            "request_id" : 123
        }
        '''
       
        faqQuestionQueryset = FaqQuestion.objects.all()
        faqQuestionSerializer = FaqQuestionSerializer(
            instance=faqQuestionQueryset, many=True
        )

        faqQuestionTranslationQueryset = FaqQuestionTranslation.objects.all()
        faqQuestionTranslationSerializer = FaqQuestionTranslationSerializer(
            instance=faqQuestionTranslationQueryset, many=True
        )

        content = {
            "faqQuestions" : faqQuestionSerializer.data,
            "faqQuestionTranslations": faqQuestionTranslationSerializer.data
        }

        return content, status.HTTP_200_OK