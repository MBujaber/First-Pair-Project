from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "seats_number",
                  "starting_time", "starting_date"]
