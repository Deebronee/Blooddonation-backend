from django.db import models

class person(models.Model):
    name = models.CharField(max_length= 100, blank=False)
    birthday = models.DateField()
    gender = models.Charfield(max_lengths= 6, blank=False)

    def __str__(self):
        return self.id