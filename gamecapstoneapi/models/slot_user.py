from django.db import models
from django.contrib.auth.models import User



class SlotUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey("Title", null=True, on_delete=models.CASCADE, related_name="user_title")
    score = models.BigIntegerField(null=True)
    session_score = models.BigIntegerField(null=True)

