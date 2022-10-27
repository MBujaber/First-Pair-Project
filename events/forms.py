from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "date", "start_time",
                  "end_time", "total_seats", "available_seats", "description", "image"]
