from django.db import models
from django.db.models.lookups import StartsWith


class Capacity(models.Model):
    start = models.DateTimeField()
    duration = models.IntegerField()
    slots = models.IntegerField()

    def get_id(self):
        return self.id

    def get_start(self):
        return self.start

    def get_duration(self):
        return self.duration

    def get_slots(self):
        return self.slots
