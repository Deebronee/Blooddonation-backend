from rest_framework.views import APIView
from rest_api.rest_api.serializers import FaqQuestionSerializer, FaqQuestionTranslationSerializer
from rest_api.models.faqQuestionTranslation import FaqQuestionTranslation
from rest_api.models.faqQuestion import FaqQuestion
from rest_framework.response import Response
from django.utils.dateparse import parse_date, parse_datetime, parse_time

class faqQuestionsList(APIView):

    def get(self, args):
        questionsQueryset = FaqQuestion.objects.all()
        translationsQueryset = FaqQuestionTranslation.objects.all()
    
        questionsSerializer = FaqQuestionSerializer(questionsQueryset, many=True)
        translationSerializer = FaqQuestionTranslationSerializer(translationsQueryset, many = True)

        content = {
            "faqQuestions" : questionsSerializer.data,
            "faqQuestionTranslations": translationSerializer.data
        }

        return Response(content)