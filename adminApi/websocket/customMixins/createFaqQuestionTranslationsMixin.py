from typing import Any, Tuple, Dict, OrderedDict
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict
from websocket.serializers import FaqQuestionTranslationSerializer


from websocket.models.faqQuestionTranslation import FaqQuestionTranslation

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class CreateFaqQuestionTranslationsMixin:
    """ Create model mixin."""

    @action()
    def createFaqQuestionTranslations(self, data: dict, **kwargs) -> Tuple[ReturnDict, int]:
        
        FaqQuestionTranslation.objects.all().delete()
        serializer = FaqQuestionTranslationSerializer(data=data, many = True)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer, **kwargs)
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED

    def perform_create(self, serializer, **kwargs):
        serializer.save()

'''
{
	"action" : "createFaqQuestionTranslations",
    "request_id" : 123,
	"data" : 
        [{	
            "head" : "Test1",
            "body" : "Test1",
            "language" : "de_DE",
            "faqQuestion" : 
                {
                    "position" : 0
                }
        },
        {	
            "head" : "Test2",
            "body" : "Test2",
            "language" : "de_DE",
            "faqQuestion" : 
                {
                    "position" : 1
                }
        }]
}
'''