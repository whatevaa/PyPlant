#!/usr/bin/env python

import datetime # from datetime import date, datetime, timedelta
import pathlib # from pathlib import Path
# using eval
import sys 
import os
# Add to sys.path the repository PyPlant/helpers, if not already in
if os.path.abspath("helpers") not in sys.path :
    sys.path.append(os.path.abspath("helpers"))
import seasons_helper # import PyPlant/helpers/seasons_helper.py

# Add to sys.path the repository PyPlant/classes, if not already in
if os.path.abspath("classes") not in sys.path :
    sys.path.append(os.path.abspath("classes"))
import plant # import PyPlant/helpers/plant.py
import calendar_event # import PyPlant/helpers/calendar_event.py



#curent_season =  seasons_helper.get_season()
#print(curent_season)

#plant_object = plant.Plant()
#seasons_helper.get_today()

def create_object(plant_name, plant_name_sc, w_spring, w_summer, w_autumn, w_winter):
    curent_season =  seasons_helper.get_season()
    # 1: Create a Plant object
    plant_object = plant.Plant() #from class Plant() in PyPlant/helpers/plant.py
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
    plant_wartering_event = calendar_event.CalendarEvent() #from class CalendarEvent() in PyPlant/helpers/calendar_event.py
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
        plant_wartering_event.last_watering_date = plant_wartering_event.last_watering(plant_wartering_event.last_watering_date, seasons_helper.get_today()) # devient today

    # 4: Store Plant object next watering
    next_watering_date = plant_wartering_event.next_watering(plant_wartering_event.last_watering_date, nb_days)
    input_dictionary = {plant_name: {"last_watering" : next_watering_date}} # update file of last watering day with the current day for watering
    # Write new dict in the file 
    with open(var_file_path, 'w') as f:
        str = repr(input_dictionary)
        f.write(str)
        f.close() # Not necessary: The files are automatically closed outside the 'with' block