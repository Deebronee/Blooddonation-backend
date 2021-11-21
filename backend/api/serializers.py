from rest_framework import fields, serializers
from backend.models import blood_donation_appointments, kill_questions

class blood_donation_appointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = blood_donation_appointments
        fields = [
            'date',
            'time' ,
            'last_name',
            'first_name',
            'reserved',
            'assigned',
        ]
        # This is so last and first name are not requiert to make a request 
        extra_kwargs = {
            'last_name' : {"required" : False},
            'first_name' : {"required" : False}
        }
        
class kill_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = kill_questions
        fields = [
            'titel',
            'question' ,
            'expected_answer',
        ]
