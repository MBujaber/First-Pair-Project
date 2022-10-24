from django.shortcuts import render
from django.http import HttpRequest, HttpResponse




def create_event(request: HttpRequest) -> HttpResponse:
    return render(request, "event-create.html")