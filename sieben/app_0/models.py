from django.db import models

# Create your models here.

from django.db.models import Q

def events_on(date):
    #TODO error handle?
    # we are trying to get events with start_date <= date && end_date >= date
    return Event.objects.filter(Q(start_date__lt=date) & Q(end_date__gt=date) )

class Event(models.Model):
    #TODO consider encapsulation / wrapper
    #TODO name and other details / photo...
    start_date = models.DateTimeField('start of the event')
    end_date = models.DateTimeField('end of the event')
    place_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Place: {self.place_name}, Start: {self.start_date}, End: {self.end_date}"