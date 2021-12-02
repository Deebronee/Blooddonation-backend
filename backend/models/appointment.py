from django.db import models
from backend.models.person import person
from backend.models.request import request

class appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    person = models.ForeignKey(person, on_delete=models.CASCADE, blank = True, null = True)
    request = models.ForeignKey(request, on_delete=models.CASCADE, blank = True, null = True)

    def get_id(self):
        return self.id

    def get_time(self):
        return self.time
