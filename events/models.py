from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events",
    )
    
    name = models.CharField(max_length=50)

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    total_seats = models.IntegerField(default=20)
    available_seats = models.IntegerField(default=20)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    image = models.ImageField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    
    booked_at = models.DateTimeField(auto_now_add=True)