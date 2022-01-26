from django.db import models

class FaqQuestion(models.Model):
    position = models.IntegerField(default = 1)

    def get_id(self):
        return self.id