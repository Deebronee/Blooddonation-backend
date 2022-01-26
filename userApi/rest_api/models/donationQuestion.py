from django.db import models


class DonationQuestion(models.Model):

    position = models.IntegerField(default = 1)
    isYesCorrect = models.BooleanField()

    def get_id(self):
        return self.id

    class Meta:
        db_table = "DonationQuestion"