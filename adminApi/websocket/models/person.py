from django.db import models

class Person(models.Model):
    name = models.CharField(max_length= 100, blank=True , null = True)
    birthday = models.DateField(blank = True, null = True)
    gender = models.CharField(max_length= 50 , blank = True, null = True)
    firstDonation = models.BooleanField(default=False, blank = True, null = True)
    telephoneNumber = models.CharField(max_length = 20, blank = True, null = True)


    def get_id(self):
        return self.id

    class Meta:
        db_table = "Person"