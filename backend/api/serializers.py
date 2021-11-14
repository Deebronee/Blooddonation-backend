from rest_framework import fields, serializers
from backend.models import blood_donation_free_appointments

class blood_donation_free_appointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = blood_donation_free_appointments
        fields = [
        'id',
        'date_time',
        'num_pacients',
        'num_taken',
        ]