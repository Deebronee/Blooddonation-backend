from datetime import datetime
from rest_framework import fields, serializers, viewsets
from backend.models.appointment import Appointment
from backend.models.donationQuestion import DonationQuestion
from backend.models.person import Person
from backend.models.request import Request
from backend.models.capacity import Capacity
from backend.models.faqQuestion import FaqQuestion



class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'birthday',
            'gender',
        ]


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = [
            'id',
            'created',
            'status',
        ]


class AppointmentSerializer(serializers.ModelSerializer):
    request = RequestSerializer(required = False)
    person = PersonSerializer(required = False)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'start',
            'duration',
            'person',
            'request',
        ]

   
    # TODO creating an appointment object should automatically create a request object 
    def create(self, validated_data):
        person_data = validated_data.pop('person')
        newPerson = Person.objects.create(**person_data)

        #request_data = validated_data.pop('request')
        newRequest = Request.objects.create(created = datetime.now(), status = "pending")
        #newRequest.created = datetime.now()
        #newRequest.status = "pending"
        newAppointment = Appointment.objects.create(person = newPerson, request = newRequest, **validated_data)

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
    
    
    
class RequestIDSerializer(serializers.ModelSerializer):
    request = RequestSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'request',
        ]    
       


class CapacitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Capacity
        fields = [
            'id',
            'start',
            'duration',
            'slots',
        ]

        
class DonationQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DonationQuestion
        fields = [
            'id'
            'titel',
            'question' ,
            'expected_answer',
        ]

class FaqQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaqQuestion
        fields =[ 
        'head'
        'body' 
        ] 

