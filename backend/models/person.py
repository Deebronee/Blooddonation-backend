from django.db import models

class person(models.Model):
    name = models.CharField(max_length= 100, blank=True , null = True)
    birthday = models.DateField(blank = True, null = True)
    gender = models.CharField(max_length= 12 , blank = True, null = True)

    def get_id(self):
        return self.id