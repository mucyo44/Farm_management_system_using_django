from django.db import models
from django.utils import timezone

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length=100)
    planting_date = models.DateField(default=timezone.now)
    harvest_date = models.DateField()
    yield_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=False , null=False,default=0)
    season = models.CharField(max_length=50,default='winter')


    def __str__(self):
        return self.name
