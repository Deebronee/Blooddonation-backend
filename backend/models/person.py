from django.db import models

class person(models.Model):
    name = models.CharField(max_length= 100, blank=False)
    birthday = models.DateField()
    gender = models.CharField(max_length= 6, blank=False)

    def get_id(self):
        return self.id