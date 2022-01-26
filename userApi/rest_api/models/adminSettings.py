from django.db import models

class AdminSettings(models.Model):

    status = models.CharField(max_length=250, blank=False)
    appointmentLength = models.IntegerField()
    
    class Meta:
        db_table = "AdminSettings"