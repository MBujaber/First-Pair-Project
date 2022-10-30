from django import forms
from .models import Event,Booking


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "date", "start_time",
                  "end_time", "total_seats", "available_seats", "description", "image"]

class BookForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["book_seats"]
        
        
 