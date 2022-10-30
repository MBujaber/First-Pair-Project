from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.db.models import Sum
from django.contrib import messages
from .models import Event
from events import models
from .forms import EventForm, BookForm
from django.contrib.auth.decorators import login_required


def get_event(request, item_id):
    item = Event.objects.get(id=item_id)
    context = {
               "item": { 
                    "id": item.id,
                    "name": item.name,
                    "date": item.date,
                    "start_time": item.start_time,
                    "end_time": item.end_time,
                    "total_seats": item.total_seats,
                    "available_seats": item.available_seats,
                    "description": item.description,
                    "user": item.user,
                    "image": item.image,
                    "created_at": item.created_at,
                    "modified_at": item.modified_at,
                }
                
            }     
    return render(request, "event_details.html", context)

def get_events(request: HttpRequest):
    event_items: list[models.Event] = list(models.Event.objects.all())
    context = {
        "event_items": event_items,
    }
    return render(request, "events_list.html", context)

@login_required
def create_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect("event-list")

    context = {"form": form}
    return render(request, "event_create.html", context)

@login_required
def update_event_item(request, item_id):
    item = Event.objects.get(id=item_id)
    form = EventForm(instance=item)
    if request.method == "POST":
        form = EventForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("event-list")
    context = {
        "item": item,
        "form": form,
    }
    return render(request, 'event_update.html', context)

@login_required
def delete_event_item(request, item_id):
    Event.objects.get(id=item_id).delete()
    return redirect("event-list")

@login_required
def book_event(request, item_id):
    item = Event.objects.get(id=item_id)
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.event = item
            form.save()
            messages.success(request, 'You have successfully booked ticket for this event, you will receive a ticket confirmation through email')
        return redirect("event-list")
    context = {
        "item": item,
        "form": form,
    }
    return render(request, "event_book.html", context)

def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")

def my_booking(request: HttpRequest) -> HttpResponse:
    return render(request, "booking_user_list.html")
    my_event
def my_event(request: HttpRequest) -> HttpResponse:
    return render(request, "my_event.html")
    
# def get_booking(request, item_id):
#     booking = Booking.objects.get(id=item_id)
#     context = {
#                "booking": { 
#                     "id": booking.id,
#                     "book_seats": booking.book_seats,
#                     "booked_at": booking.booked_at,
#                 }
#             }     
#     return render(request, "booking_user_list", context)

# def get_booking_events(request: HttpRequest):
#     booking_items: list[models.Booking] = list(models.Booking.objects.all())
#     context = {
#         "booking_items:": booking_items,
#     }
#     return render(request, "booking_user_list.html", context)
