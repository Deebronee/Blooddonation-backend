from rest_framework import fields, serializers
from backend.models.appointment import appointment
from backend.models.donationQuestion import donationQuestion
from backend.models.person import person
from backend.models.request import request

class appointmentSerializer(serializers.ModelSerializer):
    person_id = serializers.CharField(source = 'person.id')
    request_id = serializers.CharField(sorce = 'request.id')

    class Meta:
        model = appointment
        fields = [
            'id',
            'start',
            'duration',
            'person_id',
            'request_id',
        ]


class personSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = person
        fields = [
            'id',
            'name'
            'birthday'
            'gender',
        ]


class RequestSerializer(serializers.ModelSerializer):
    appointment_id = serializers.CharField(source = 'appointmend.id')

    class Meta:
        model = appointment
        fields = [
            'id',
            'created',
            'status',
            'appointment_id',
        ]

        
class donationQuestion(serializers.ModelSerializer):
    class Meta:
        model = donationQuestion
        fields = [
            'titel',
            'question' ,
            'expected_answer',
        ]

