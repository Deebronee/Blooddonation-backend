from django.db import models

class request(models.Model):
    created = models.DateTimeField() 
    status = models.CharField(max_length=10, blank=False)

    def get_id(self):
        return self.id