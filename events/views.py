from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event
from events import models
from .forms import EventForm


def get_event(request, item_id):
    item = Event.objects.get(id=item_id)
    context = {
               "item": { 
                    "id": item.id,
                    "name": item.name,
                    "description": item.description,
                    "seats_number": item.seats_number,
                    "user": item.user
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
        form = EventForm(request.POST)
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
