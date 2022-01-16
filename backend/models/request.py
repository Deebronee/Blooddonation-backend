from datetime import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver




class Request(models.Model):
    created = models.DateTimeField() 
    status = models.CharField(max_length=10, blank=False)

    def get_id(self):
        return self.id


