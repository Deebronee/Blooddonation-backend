from django.db import models
from django.db.models.fields import DateTimeCheckMixin, DateTimeField
# model classes pulling data from daterbase
# Create your models here.


# Create your models here. pull data from database and present to user

    

class blood_donation_free_appointments(models.Model):
    date_time = models.DateTimeField()
    num_pacients = models.IntegerField(default=0)
    num_taken = models.IntegerField(default=0)
    def __str__(self):
        return 'free'

class blood_donation_appointments(models.Model):
    # The ID is generated automaticly
    date_time = models.ForeignKey(blood_donation_free_appointments, on_delete=models.CASCADE) # date and time of appointment
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    def __str__(self):
        return self.date_time