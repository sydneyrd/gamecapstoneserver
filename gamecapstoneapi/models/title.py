from django.db import models

class Title(models.Model): 
    label = models.CharField(max_length=100)
