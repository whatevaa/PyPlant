#!/usr/bin/env python

import sys
import datetime # from datetime import date, datetime, timedelta
import calendar
import numpy as np
import pathlib # from pathlib import Path
import pickle
import os
# using eval


##########################
# Variable and Functions #
##########################
date = datetime.date

# 1: Get Current season
# use of today (the current day / year) to find season
today = date.today()
Y= date.today().year

seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

def get_season(now):
    return next(season for season, (start, end) in seasons
                if start <= now <= end)

curent_season = get_season(today)


#########
# Class #
#########
class Plant:
    name = "plant_name" # Name
    name_sc = "nom_scientifique" # Scientific name
    watering = {
        "w_spring": 0, # Spring watering (in days)
        "w_summer": 0, # Summer watering (in days)
        "w_autumn": 0, # Autumn watering (in days)
        "w_winter": 0 # Winter watering (in days)
    }

    def nb_days_watering(self, season: str, watering_dict: dict) -> int:
        day_watering = ""
        match season :
            case "winter" :
                print("winter")
                day_watering = watering_dict["w_winter"]
            case "spring" :
                print("spring")
                day_watering = watering_dict["w_spring"]
            case "summer" :
                print("summer")
                day_watering = watering_dict["w_summer"]
            case "autumn" :
                print("autumn")
                day_watering = watering_dict["w_autumn"]
        return day_watering


class CalendarEvent:
    last_watering_date = (0, 0, 0)

    def last_watering(self, date, today):
        if(date == (0, 0, 0)):
            date = today #else prendre la version update
        return date
    
    def next_watering(self, last_date, nb_days):
        return last_date + datetime.timedelta(days=nb_days) # next_date = last_date + datetime.timedelta(days=nb_days)


##########################
# Function create object #
##########################

def create_object(plant_name, plant_name_sc, w_spring, w_summer, w_autumn, w_winter, curent_season):
    # 1: Create a Plant object
    plant_object = Plant()
    plant_object.name = plant_name
    plant_object.name_sc = plant_name_sc
    plant_object.watering = {"w_spring": w_spring, # Spring watering (in days)
        "w_summer": w_summer, # Summer watering (in days)
        "w_autumn": w_autumn, # Autumn watering (in days)
        "w_winter": w_winter # Winter watering (in days)
        }
    # nb days until next watering
    nb_days = plant_object.nb_days_watering(curent_season, plant_object.watering)

    # 2: Create event of watering object (specific for a Plant in particular) and file to store last watering date
    plant_wartering_event = CalendarEvent()
    var_file_path = pathlib.Path("variables_calendar_watering_" + plant_object.name + ".txt") # File of last watering date

    # 3: Read file (if exist) to find last watering date of this plant object
    if var_file_path.is_file():
    # file exists
        with open(var_file_path, 'r') as f:
            contents= f.read()
            res = eval(contents) # eval => str to dict
            plant_dict = res[plant_name]
            plant_wartering_event.last_watering_date = plant_dict["last_watering"]
            f.close() # Not necessary: The files are automatically closed outside the 'with' block
    else :
        plant_wartering_event.last_watering_date = plant_wartering_event.last_watering(plant_wartering_event.last_watering_date, today) # devient today

    # 4: Store Plant object next watering
    next_watering_date = plant_wartering_event.next_watering(plant_wartering_event.last_watering_date, nb_days)
    input_dictionary = {plant_name: {"last_watering" : next_watering_date}} # update file of last watering day with the current day for watering
    # Write new dict in the file 
    with open(var_file_path, 'w') as f:
        str = repr(input_dictionary)
        f.write(str)
        f.close() # Not necessary: The files are automatically closed outside the 'with' block



########
# Main #
########

create_object("caoutchouc", "ficus elastica", 7, 7, 12, 12, curent_season)
create_object("pilea", "pilea peperomioides", 7, 7, 9, 12, curent_season)