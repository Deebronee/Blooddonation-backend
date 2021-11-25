
from django.db import models


class appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    last_name = models.CharField(max_length=100 , blank=True)
    first_name = models.CharField(max_length=100 , blank=True)
    reserved = models.BooleanField()
    assigned = models.BooleanField()
    def __str__(self):
        return self.id