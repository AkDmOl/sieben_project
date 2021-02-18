from django.db import models

# Create your models here.

class Event(models.Model):
    #TODO start / end time + create separate class?
    start_date = models.DateTimeField('start of the event')
    end_date = models.DateTimeField('end of the event')

    place_name = models.CharField(max_length=100)
    #TODO name and other details / photo...

    def __str__(self):
        return f"Place: {self.place_name}, Start: {self.start_date}, End: {self.end_date}"