from django.db import models

class faqQuestion(models.Model):
    head = models.CharField(max_length= 100, blank=False)
    body = models.TextField(max_length= 500, blank=False)

    def get_id(self):
        return self.id