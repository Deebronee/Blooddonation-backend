from django.db import models
from backend.models import appointment

class request(models.Model):
    created = models.DateTimeField() 
    status = models.CharField(max_length=10, blank=False)
    appointment = models.ForeignKey(appointment, on_delete=models.CASCADE)

    def __str__(self):
        return self.id