from django.db import models
from backend.models.person import person
from backend.models.request import request
from datetime import datetime

class appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    #duration = models.DurationField()
    duration = models.IntegerField()
    person = models.ForeignKey(person, on_delete=models.CASCADE, blank = True, null = True)
    request = models.ForeignKey(request, on_delete=models.CASCADE, blank = True, null = True)

    def get_id(self):
        return self.id

    def get_time(self):
        return str(self.time)

    def get_time_hour(self):
        return self.time.hour

    def get_duration(self):
        return int(self.duration)

