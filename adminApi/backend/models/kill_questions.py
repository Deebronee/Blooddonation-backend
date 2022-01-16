from django.db import models


class kill_questions(models.Model):
    titel = models.CharField(max_length=100)
    question = models.TextField()
    expected_answer = models.BooleanField()
    def __str__(self):
        return self.titel