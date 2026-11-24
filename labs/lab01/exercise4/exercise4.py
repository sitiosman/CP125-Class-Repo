# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour) :
    is_night = hour >= 22 or hour <= 6
    
    if vehicle_type == "Electric":
        return 2.0
    if vehicle_type == "Hybrid":
        if is_night :
            return 2.0
        return 5.0
    return 5.0
        