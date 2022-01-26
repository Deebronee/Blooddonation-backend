from django.db import models
from websocket.models.faqQuestion import FaqQuestion

class FaqQuestionTranslation(models.Model):
    head = models.CharField(max_length=250, blank=False)
    body = models.TextField(blank=False)
    language = models.CharField(max_length=250, blank=False)
    faqQuestion = models.ForeignKey(FaqQuestion, on_delete=models.CASCADE, null = False, blank = False)

    def get_id(self):
        return self.id