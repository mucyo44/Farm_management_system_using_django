from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

    
class FarmActivity(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField() 
    @property
    def is_completed(self):
        return date.today() >= self.end_date
 



    def __str__(self):
        return self.name 
    

  


