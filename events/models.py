from django.db import models
from users.forms import User


class Event(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events",
    )
    
    name = models.CharField(max_length=50)

    starting_time = models.TimeField()
    starting_date = models.DateField()

    seats_number = models.IntegerField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    image = models.ImageField()

    def __str__(self):
        return self.name
