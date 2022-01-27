from django.db import models
from rest_api.models.person import Person
from rest_api.models.request import Request as r
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
import json

class Appointment(models.Model):
    #date = models.DateField()
    #time = models.TimeField()
    start = models.DateTimeField()
    #duration = models.DurationField()
    duration = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank = True, null = True)
    request = models.ForeignKey(r, on_delete=models.CASCADE, blank = True, null = True)

    def get_id(self):
        return self.id

    def get_start(self):
        return self.start

    def get_time_hour(self):
        return self.time.hour

    def get_duration(self):
        return int(self.duration)

    '''
    def save(self, *args, **kwargs):
        if self.pk is None:  # create
            self.request = r.objects.create(created = datetime.now(), status = "pending")
        super().save(*args, **kwargs)  # Call the "real" save() method.
    '''

    #def post(self, request, format = json)
    #    serializer = app

    class Meta:
        db_table = "Appointment"
