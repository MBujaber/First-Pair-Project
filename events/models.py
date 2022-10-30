from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator 

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

    total_seats = models.PositiveIntegerField(default=20)
    available_seats = models.PositiveIntegerField(default=20)

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
    book_seats = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    booked_at = models.DateTimeField(auto_now_add=True)



        
    def __str__(self):
        return f"By: {self.user} - Event: {self.event} - Seats:{self.book_seats}"

    def validate_nonzero(value):
        if value == 0:
            raise ValidationError(('Quantity %(value)s is not allowed'),
                params={'value': value},
            )

    # @property
    # def available(self):
    #     available_seats = []
    #     seats = self.book_seats
    #     for seat in seats:
    #        num = seat + s
    #         return 