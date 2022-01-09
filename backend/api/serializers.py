from datetime import datetime
from rest_framework import fields, serializers, viewsets
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
    request = requestSerializer()
    person = personSerializer(required = False)

    class Meta:
        model = appointment
        fields = [
            'id',
            'start',
            'duration',
            'person',
            'request',
        ]

    
    def create(self, validated_data):
        person_data = validated_data.pop('person')
        newPerson = person.objects.create(**person_data)

        #request_data = validated_data.pop('request')
        newRequest = request.objects.create(created = datetime.now(), status = "pending")
        #newRequest.created = datetime.now()
        #newRequest.status = "pending"

        newAppointment = appointment.objects.create(person = newPerson, request = newRequest, **person_data)

        return newAppointment


    def update(self, instance, validated_data):
        request_data = validated_data.pop('request')
        newRequest = instance.request

        instance.start = validated_data.get('start', instance.start)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()

        newRequest.created = request_data.get('created', newRequest.created)
        newRequest.status = request_data.get('status', newRequest.status)
        newRequest.save()

        return instance
    
    
    



class requestIDSerializer(serializers.ModelSerializer):
    request = requestSerializer(read_only=True)

    class Meta:
        model = appointment
        fields = [
            'id',
            'request',
        ]    
       


class capacitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = capacity
        fields = [
            'id',
            'start',
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

