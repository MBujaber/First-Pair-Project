from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse
from .models import Event
from events import models
from .forms import EventForm


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


def delete_event_item(request, item_id):
    Event.objects.get(id=item_id).delete()
    return redirect("event-list")


def book_ticket(request):

    if request.user.is_authenticated:
        movie_show = Event.objects.get()
        if movie_show:
            if (movie_show.event.available_seats >= 1):
                movie_show.event.available_seats -= 1
                movie_show.event.save()
                return JsonResponse({"message": "You have successfully booked ticket for this show"})
            else:
                return JsonResponse({"message": "There are no Seats available for this Show"})
        else:
            return JsonResponse({"message": "Booking failed as the selected preferences are incorrect/in valid"})
    return JsonResponse({"message": "Kindly login to continue booking for your favorite movie now"})


