from django.db import models


class DonationQuestion(models.Model):
    body = models.TextField()
    isYesCorrect = models.BooleanField()

    def get_id(self):
        return self.id