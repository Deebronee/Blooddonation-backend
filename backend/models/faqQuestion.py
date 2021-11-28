from django.db import models
from django.db.models.fields import CharField

class faqQuestion(models.Model):
    head = models.CharField(max_length= 100, blank=False)
    body = models.CharField(max_length= 500, blank=False)

    def __str__(self):
        return self.id