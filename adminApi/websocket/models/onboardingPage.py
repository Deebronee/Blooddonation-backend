from django.db import models


class OnboardingPage(models.Model):
    position = models.IntegerField()
    head = models.CharField(max_length=250, blank=False)
    body = models.TextField(max_length=250, blank=False)
    image = models.CharField(max_length=250, blank=False)

    def get_id(self):
        return self.id

    class Meta:
        db_table = "OnboardingPage"