from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)

    starting_time = models.TimeField()
    starting_date = models.DateField()

    seats_number = models.IntegerField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
