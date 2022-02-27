from django.db import models
from websocket.models.donationQuestion import DonationQuestion

class DonationQuestionTranslation(models.Model):
    id = models.IntegerField(primary_key = True)
    body = models.TextField(blank=False)
    language = models.CharField(max_length=10, blank=False)
    donationQuestion = models.IntegerField()

    def get_id(self):
        return self.id

    class Meta:
        db_table = "DonationQuestionTranslation"