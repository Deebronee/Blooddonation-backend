from django.db import models

class FaqQuestion(models.Model):

    id = models.IntegerField(primary_key=True)
    position = models.IntegerField(default = 0)

    def get_id(self):
        return self.id

    class Meta:
        db_table = "FaqQuestion"