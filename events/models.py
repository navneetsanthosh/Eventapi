from django.db import models

from accounts.models import MyUser


# Create your models here.
class Event(models.Model):
    organizer = models.ForeignKey(MyUser,on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name