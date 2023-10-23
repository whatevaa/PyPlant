#!/usr/bin/env python

# Creation of Plant class
class Plant:
    name = "plant_name" # Name
    name_sc = "nom_scientifique" # Scientific name
    watering = {
        "w_spring": 0, # Spring watering (in days) - 0 default
        "w_summer": 0, # Summer watering (in days) - 0 default
        "w_autumn": 0, # Autumn watering (in days) - 0 default
        "w_winter": 0 # Winter watering (in days) - 0 default
    }

    def nb_days_watering(self, season: str, watering_dict: dict) -> int:
        day_watering = ""
        match season :
            case "winter" :
                #print("winter")
                day_watering = watering_dict["w_winter"]
            case "spring" :
                #print("spring")
                day_watering = watering_dict["w_spring"]
            case "summer" :
                #print("summer")
                day_watering = watering_dict["w_summer"]
            case "autumn" :
                #print("autumn")
                day_watering = watering_dict["w_autumn"]
        return day_watering