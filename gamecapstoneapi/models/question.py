from django.db import models


class Question(models.Model):
    label = models.CharField(max_length=500)
    difficulty = models.FloatField()
    solutions = models.ManyToManyField("Solution", through='QuestionSolution', related_name="question_solution")
