#!/usr/bin/env python

import datetime # from datetime import date, datetime, timedelta

def get_today():
    date = datetime.date
    return date.today()

# 1: Get Current season
def get_season()-> str:
    # Use of today (current day / year) to find season
    date = datetime.date
    today = date.today()
    Y= date.today().year

    # Seasons table
    seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
            ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
            ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
            ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
            ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]
    
    return next(season for season, (start, end) in seasons
                if start <= today <= end)