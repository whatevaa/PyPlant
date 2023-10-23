#!/usr/bin/env python

import datetime # from datetime import date, datetime, timedelta

# Creation of Calendat event class
class CalendarEvent:
    last_watering_date = (0, 0, 0)

    def last_watering(self, date, today):
        if(date == (0, 0, 0)):
            date = today #else prendre la version update
        return date
    
    def next_watering(self, last_date, nb_days):
        return last_date + datetime.timedelta(days=nb_days) # next_date = last_date + datetime.timedelta(days=nb_days)