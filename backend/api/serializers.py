from rest_framework import fields, serializers
from backend.models import blood_donation_free_appointments

class blood_donation_free_appointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = blood_donation_free_appointments
        fields = [
            'date',
            'time' ,
            'last_name',
            'first_name',
            'reserved',
            'assigned',
        ]