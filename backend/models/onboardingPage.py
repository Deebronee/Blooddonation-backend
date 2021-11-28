from django.db import models

class onboardingPage(models.Model):
    position = models.IntegerField()
    head = models.CharField(max_length=250, blank=False)
    body = models.CharField(max_length=250, blank=False)
    image = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.id