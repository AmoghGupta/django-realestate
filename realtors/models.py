from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_dates = models.DateTimeField(default = datetime.now, blank=True)
    
    #this has nothing to do with sql concepts..this just for admin area
    # when a new record is added to this model, it will be highlighted as "name"
    # this is done so that any data in this model is represented by name (as main)
    def __str__(self):
        return self.name


