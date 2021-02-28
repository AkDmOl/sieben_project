from django.utils.timezone import now
from datetime import timedelta
from .models import events_on
from .date_utils import days_range

# Event Calendar handles dict of (day: [events]) pairs  
class EventCalendar:
    def __init__(self):
        self.days = {}
    
    def __str__(self):
        return str(self.days)

    def load_for(self, w=0, d=0):
        today = now()
        future = today + timedelta(weeks=w, days=d)
        for d in days_range(today, future):
            #TODO if error/exception appears return False
            #more user-friendly approach at first
            events_str = []
            for ev_mod in events_on(d):
                events_str.append(str(ev_mod) + "<br>")
            
            #TODO switch to self.days[d] = events_on(d).values()
            self.days[d] = events_str
        return True
    
    def load_for_week(self):
        return self.load_for(w=1)