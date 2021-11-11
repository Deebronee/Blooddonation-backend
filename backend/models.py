from django.db import models
from django.db.models.fields import DateTimeCheckMixin, DateTimeField
# model classes pulling data from daterbase
# Create your models here.


# Create your models here. pull data from database and present to user
class blood_donation_appointments(models.Model):
    # The ID is generated automaticly
    Date_time = models.DateTimeField() # date and time of appointment
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

class blood_donation_free_appointments(models.Model):
    Date_time = models.DateTimeField()
    num_pacients = models.IntegerField(default=0)
    num_taken = models.IntegerField(default=0)