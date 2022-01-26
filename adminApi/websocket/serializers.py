from datetime import datetime
from rest_framework import fields, serializers, viewsets
from websocket.models.appointment import Appointment
from websocket.models.donationQuestion import DonationQuestion
from websocket.models.person import Person
from websocket.models.request import Request
from websocket.models.capacity import Capacity
from websocket.models.faqQuestion import FaqQuestion
from websocket.models.donationQuestionTranslation import DonationQuestionTranslation
from websocket.models.faqQuestionTranslation import FaqQuestionTranslation
from websocket.models.adminSettings import AdminSettings
from websocket.models.statistic import Statistic



class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'birthday',
            'gender',
            'firstDonation',
            'telephoneNumber'
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
    request = RequestSerializer(required=True)
    person = PersonSerializer(required=True)

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
        request_data = validated_data.pop('request')
        person_data = validated_data.pop('person')
        
        newRequest = Request.objects.create(**request_data)
        newPerson = Person.objects.get_or_create(**person_data)[0]
        newAppointment = Appointment.objects.create(request=newRequest, person=newPerson, **validated_data)
        
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
            'id',
            'position',
            'isYesCorrect',
        ]

class DonationQuestionTranslationSerializer(serializers.ModelSerializer):
    donationQuestion = DonationQuestionSerializer(required = True)

    class Meta:
        model = DonationQuestionTranslation
        fields =[ 
        'id', 
        'head',
        'body',
        'language',
        'donationQuestion',
        ] 
        
    def create(self, validated_data):
        donationQuestion_data = validated_data.pop('donationQuestion')
        
        newDonationQuestion = DonationQuestion.objects.create(**donationQuestion_data)
        newDonationQuestionTranslation = DonationQuestionTranslation.objects.create(donationQuestion=newDonationQuestion, **validated_data)
        
        return newDonationQuestionTranslation

    def update(self, instance, validated_data):
        donationQuestion_data = validated_data.pop('donationQuestion')
        newDonationQuestion = instance.donationQuestion

        instance.head = validated_data.get('head', instance.head)
        instance.body = validated_data.get('body', instance.body)
        instance.language = validated_data.get('language', instance.language)
        instance.save()

        newDonationQuestion.position = donationQuestion_data.get('position', newDonationQuestion.position)
        newDonationQuestion.isYesCorrect = donationQuestion_data.get('isYesCorrect', newDonationQuestion.isYesCorrect)
        newDonationQuestion.save()

        return instance

class FaqQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FaqQuestion
        fields =[ 
        'id', 
        'position',
        ] 

class FaqQuestionTranslationSerializer(serializers.ModelSerializer):
    faqQuestion = FaqQuestionSerializer(required = True)

    class Meta:
        model = FaqQuestionTranslation
        fields =[ 
        'id', 
        'head',
        'body',
        'language',
        'faqQuestion',
        ] 

    def create(self, validated_data):
        faqQuestion_data = validated_data.pop('faqQuestion')
        newFaqQuestion = FaqQuestion.objects.create(**faqQuestion_data)
        newFaqQuestionTranslation = FaqQuestionTranslation.objects.create(faqQuestion=newFaqQuestion, **validated_data)
        return newFaqQuestionTranslation


    def update(self, instance, validated_data):
        faqQuestion_data = validated_data.pop('faqQuestion')
        newFaqQuestion = instance.faqQuestion

        instance.head = validated_data.get('head', instance.head)
        instance.body = validated_data.get('body', instance.body)
        instance.language = validated_data.get('language', instance.language)
        instance.save()

        newFaqQuestion.position = faqQuestion_data.get('position', newFaqQuestion.position)
        newFaqQuestion.save()

        return instance

class AdminSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminSettings
        fields = [
            'id',
            'status',
            'appointmentLength',
        ]

class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = [
            'id',
            'numberOfFirstTimeDonations',
            'totalBookedAppointments',
            'aged18to27',
            'aged28to37',
            'aged38to47',
            'aged48to57',
            'aged58to68',
            'acceptedRequests',
            'rejectedRequests',
            'cancelledRequests',
        ]