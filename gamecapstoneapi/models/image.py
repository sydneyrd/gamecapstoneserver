from django.db import models

class Image(models.Model):
    label = models.CharField(max_length=200)
    action_pic = models.ImageField(
        upload_to='assets', height_field=None,
        width_field=None, max_length=None, null=True)