from django.db import models


class DonationQuestion(models.Model):

    id = models.IntegerField(primary_key = True)
    position = models.IntegerField(default = 0)
    isYesCorrect = models.BooleanField()

    def get_id(self):
        return self.id

    class Meta:
        db_table = "DonationQuestion"