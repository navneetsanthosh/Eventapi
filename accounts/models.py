from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    role_choices = (('organizer','Organizer'),
                    ('customer','Customer'),)

    #(value stored in db,value displayed in django form/admin)
    role = models.CharField(max_length=100,choices=role_choices,default='customer')
    phone = models.IntegerField(null=True,blank=True)



