from django.db import models
from django.utils import timezone
# Create your models here.


class Records(models.Model):

    animal_type = models.CharField(max_length=100)
    birth_date = models.DateField()
    status = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)



    def __str__(self):
        return self.animal_type


