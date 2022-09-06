from django.db import models


class QuestionSolution(models.Model):
    solution = models.ForeignKey("Solution", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
