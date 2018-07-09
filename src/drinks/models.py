from django.db import models

# Create your models here.
class DrinkInfo(models.Model):
    name                = models.CharField(max_length=120)
    place_of_origin     = models.CharField(max_length=120, null=True, blank=True)
    description         = models.CharField(max_length=240, null=True, blank=True)