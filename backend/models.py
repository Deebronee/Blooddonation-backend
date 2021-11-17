from django.db import models
# model classes pulling data from daterbase
# Create your models here.


# Create your models here. pull data from database and present to user

    

class blood_donation_free_appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    reserved = models.BooleanField(default=0)
    assigned = models.BooleanField(default=0)
    def __str__(self):
        return self.pk

    
class kill_questions(models.Model):
    titel = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    expected_answer = models.BooleanField()
    def __str__(self):
        return self.titel