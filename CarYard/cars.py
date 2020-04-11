# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:21:07 2019

@author: upoudel
"""

import vehicle

# Collection of Car objects in a List
cars = []

"""  
   Task 6:  Implement addCar(...) function

  *The function creates a Car object using the parameters provided, and adds to its collection of cars

"""


def add_car(rego, model, color, price):
    cars.append(vehicle.Car(rego, model, color, price))


"""
   Task 7:  Implement removeCar(...) function

  *The function removes a Car with a matching rego (parameter) from its collection of car

"""


def remove_car(rego):
    for car in cars:
        if car.rego == rego:
            cars.remove(car)
            break


"""
   Task 8:  Implement all_cars() function

  *The function returns - all cars in the collection

"""


def all_cars():
    return cars


"""
   Task 9:  Implement search() function

  *The function returns a car matching the rego parameter from its collection of cars

"""


def search(rego):
    for car in cars:
        if car.rego == rego:
            return car
