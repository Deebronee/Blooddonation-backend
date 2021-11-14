from django.db import models
from django.db.models.deletion import CASCADE
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
    year=models.IntegerField(default=1)
    month=models.IntegerField(default=1)
    day=models.IntegerField(default=1)
    hour=models.IntegerField(default=1)
    minute=models.IntegerField(default=1)
    number_available=models.IntegerField(default=1)
    text=models.TextField(default="text")
    ymdhm=models.TextField(default=str(year)+str(month)+str(day)+str(hour)+str(minute))
    def __str__(self):
        return str(self.year)+str(self.month)+str(self.day)+str(self.hour)+str(self.minute)
    
class Individual_appointment(models.Model):
    reservation=models.BooleanField()
    booked=models.BooleanField()
    status=models.TextField(default="no status")
    appointment_time=models.ForeignKey(blood_donation_free_appointments, on_delete=CASCADE, default="1")
    
    def __str__(self):
        return self.status
        
