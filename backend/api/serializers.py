from rest_framework import fields, serializers
from backend.models.appointments import appointments
from backend.models.kill_questions import kill_questions

class appointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointments
        fields = [
            'date',
            'time',
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
