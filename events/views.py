from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Event
from events import models
from .forms import EventForm


def get_event(request: HttpRequest) -> HttpResponse:
    events: list[models.Event] = list(models.Event.objects.all())
    context = {
        "events": events,
    }
    return render(request, "event-list.html", context)


def create_event(request):
    form = EventForm()
    if request.method == "POST":
        _form = EventForm(request.POST)
        if _form.is_valid():
            _form.save()
        return redirect("home")

    context = {"form": form}
    return render(request, "event-create.html", context)
