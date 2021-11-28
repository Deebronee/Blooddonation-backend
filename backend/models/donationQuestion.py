from django.db import models


class kill_questions(models.Model):
    body = models.TextField()
    isYesCorrect = models.BooleanField()

    def __str__(self):
        return self.id