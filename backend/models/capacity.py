from django.db import models
from django.db.models.lookups import StartsWith


class capacity(models.Model):
    start = models.DateTimeField()
    duration = models.DurationField()
    slots = models.IntegerField()

    def __str__(self):
        return self.id