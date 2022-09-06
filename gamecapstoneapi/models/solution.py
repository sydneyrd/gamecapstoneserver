from django.db import models

class Solution(models.Model):
    label = models.CharField(max_length=100)