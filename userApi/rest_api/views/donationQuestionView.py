from rest_framework.views import APIView
from rest_api.rest_api.serializers import DonationQuestionSerializer, DonationQuestionTranslationSerializer
from rest_api.models.donationQuestion import DonationQuestion
from rest_api.models.donationQuestionTranslation import DonationQuestionTranslation
from rest_framework.response import Response



class donationQuestionList(APIView):

    def get(self, args):
        questionsQueryset = DonationQuestion.objects.all()
        translationsQueryset = DonationQuestionTranslation.objects.all()
    
        questionsSerializer = DonationQuestionSerializer(questionsQueryset, many=True)
        translationSerializer = DonationQuestionTranslationSerializer(translationsQueryset, many = True)

        content = {
            "donationQuestions" : questionsSerializer.data,
            "donationQuestionTranslations": translationSerializer.data
        }

        return Response(content)