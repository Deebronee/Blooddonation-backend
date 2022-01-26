from django.db import models


class DonationQuestion(models.Model):

    position = models.IntegerField(default = 0)
    isYesCorrect = models.BooleanField()

    def get_id(self):
        return self.id