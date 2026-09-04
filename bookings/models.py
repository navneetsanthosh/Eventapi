from django.db import models

from events.models import Event

from accounts.models import MyUser


# Create your models here.
class Booking(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    seats = models.IntegerField()
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,default='pending')

    def __str__(self):
        return self.event.name

