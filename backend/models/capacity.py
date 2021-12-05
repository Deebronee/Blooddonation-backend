from django.db import models
from django.db.models.lookups import StartsWith


class capacity(models.Model):
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    slots = models.IntegerField()

    def get_id(self):
        return self.id

    def get_time(self):
        return str(self.time)

    def get_duration(self):
        return self.duration

    def get_slots(self):
        return self.slots
