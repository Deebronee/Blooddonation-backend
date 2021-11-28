from django.db import models


class donationQuestion(models.Model):
    body = models.TextField()
    isYesCorrect = models.BooleanField()

    def get_id(self):
        return self.id