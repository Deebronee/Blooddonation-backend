from typing import Any, Tuple, Dict, OrderedDict
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict
from websocket.serializers import DonationQuestionTranslationSerializer

from websocket.models.donationQuestionTranslation import DonationQuestionTranslation

from .decorators import action
from djangochannelsrestframework.settings import api_settings

class CreateDonationQuestionTranslationsMixin:
    """ Create model mixin."""

    @action()
    def createDonationQuestionTranslations(self, data: dict, **kwargs) -> Tuple[ReturnDict, int]:
        
        DonationQuestionTranslation.objects.all().delete()
        serializer = DonationQuestionTranslationSerializer(data=data, many = True)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer, **kwargs)
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED

    def perform_create(self, serializer, **kwargs):
        serializer.save()

'''
{
	"action" : "createDonationQuestionTranslations",
    "request_id" : 123,
	"data" : 
        [{	
            "head" : "Test1",
            "body" : "Test1",
            "language" : "de_DE",
            "donationQuestion" : 
                {
                    "position" : 0,
                    "isYesCorrect" : true
                }
        },
        {	
            "head" : "Test2",
            "body" : "Test2",
            "language" : "de_DE",
            "donationQuestion" : 
                {
                    "position" : 1,
                    "isYesCorrect" : false
                }
        }]
}
'''