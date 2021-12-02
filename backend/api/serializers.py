from rest_framework import fields, serializers
from backend.models.appointment import appointment
from backend.models.donationQuestion import donationQuestion
from backend.models.person import person
from backend.models.request import request
from backend.models.capacity import capacity
from backend.models.faqQuestion import faqQuestion



class personSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = person
        fields = [
            'id',
            'name',
            'birthday',
            'gender',
        ]


class requestSerializer(serializers.ModelSerializer):

    class Meta:
        model = request
        fields = [
            'id',
            'created',
            'status',
        ]


class appointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = appointment
        fields = [
            'id',
            'date',
            'time',
            'duration',
            'person',
            'request',
        ]

    
       


class capacitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = capacity
        fields = [
            'id',
            'date',
            'time',
            'duration',
            'slots',
        ]

        
class donationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = donationQuestion
        fields = [
            'id'
            'titel',
            'question' ,
            'expected_answer',
        ]

class faqQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = faqQuestion
        fields =[ 
        'head'
        'body' 
        ] 

