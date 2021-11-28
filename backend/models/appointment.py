from django.db import models
from backend.models import person, request

class appointment(models.Model):
    start = models.DateTimeField()
    duration = models.DurationField()
    person = models.ForeignKey(person, on_delete=models.CASCADE)
    request = models.ForeignKey(request, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

