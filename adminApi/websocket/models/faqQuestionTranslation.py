from django.db import models
from websocket.models.faqQuestion import FaqQuestion

class FaqQuestionTranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    head = models.TextField(blank=False)
    body = models.TextField(blank=False)
    language = models.CharField(max_length=10, blank=False)
    faqQuestion = models.IntegerField()

    def get_id(self):
        return self.id

    class Meta:
        db_table = "FaqQuestionTranslation"