from django.db import models

class Feedback(models.Model):
    comment = models.CharField(max_length=1000)
    slot_user = models.ForeignKey("SlotUser", on_delete=models.CASCADE, related_name="slot_user" )
    contact = models.CharField(max_length=200)
    