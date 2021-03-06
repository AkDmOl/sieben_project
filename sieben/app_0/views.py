from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .calendar import EventCalendar
from .models import Event

""" Debug all
def index(request):
    return HttpResponse(Event.objects.all())
"""

def index(request):
    ev_cal = EventCalendar()
    if not ev_cal.load_for_week():
        #TODO appropriate error response
        return HttpResponse("Failed to load events") 
    return render(request, "app_0/index.html", {
        "calendar" : ev_cal.days
    })