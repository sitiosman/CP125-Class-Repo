# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient(one_way_km, budget):
    round_trip = one_way_km * 2
    fuel_litres = round_trip / 10
    total_cost = fuel_litres * 2
    if total_cost <= budget:
        return True
    else :
        return False
