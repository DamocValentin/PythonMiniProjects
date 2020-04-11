# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:21:07 2019

@author: upoudel
"""
import cars


def load_cars():
    cars.add_car("Y100", "Toyota", "Red", 10000)
    cars.add_car("Y200", "Subaru", "Blue", 20000)
    cars.add_car("Y300", "Ford", "Green", 30000)


"""  
   Task 2:  Implement buy_car() function

   buy_car function adds a new car to the Car yards's collection of cars. 
   Car rego(registration) value must not match the existing rego.  Duplicate rego message is shown
   until a new rego is provided. 

  *See the screen shot provided: buy_car
"""


def buy_car():
    print('\tBuy Car')
    print('----------------------')

    while True:

        rego = input('Enter Rego:')
        for car in cars.all_cars():
            if car.rego == rego:
                print('----------------------')
                print('Duplicate rego. Enter new value')
                continue

        model = input('Enter Model:')
        color = input('Enter Color:')

        price = int(input('Enter Price:'))
        cars.add_car(rego, model, color, price)
        print('----------------------')
        print('Car added: ' + model)
        break

"""
   Task 3:  Implement sell_car() function

   sell_car function removes an existing Car from its collection of cars. Function prompts the user for a car
   rego(registration) to locate the car for sale. Incorrect rego message is shown until a vaild rego is provided.

   The output of a sold car includes a selling price which is a markup of (30%) of the purchase price


  *See the screen shot provided: sell_car
"""


def sell_car():
    print('\tSell Car')
    print('----------------------')

    not_found = True
    my_rego = ''
    while not_found:
        rego = input('Enter Car Rego:')
        for car in cars.all_cars():
            if car.rego == rego:
                not_found = False
                my_rego = rego
        if not_found:
            print('Incorrect rego: ' + rego + '\n')

    car = cars.search(my_rego)

    print('Car Model:' + car.model)
    print('Car Color: ' + car.color)
    print('Car Purchase price: $' + str(car.price))
    print('Car Sell price: $' + str(car.price + (car.price*30)/100))

    cars.remove_car(my_rego)



"""
   Task 4:  Implement search_car() function

   search_car function shows the details of an existing car. The user must provide an existing car rego for searching.
   Incorrect rego message is shown until a vaild rego is provided.

  *See the screen shot provided: search_car
"""


def search_car():
    print('\tSell Car')
    print('----------------------')

    not_found = True
    my_rego = ''
    while not_found:
        rego = input('Enter Car Rego:')
        for car in cars.all_cars():
            if car.rego == rego:
                not_found = False
                my_rego = rego
        if not_found:
            print('Incorrect rego: ' + rego + '\n')

    car = cars.search(my_rego)
    print()
    print('Car Model: ' + car.model)
    print('Car Color: ' + car.color)
    print('Car Price: $' + str(car.price))


"""
   Task 5:  Implement search_car() function

   list_all_cars function shows the details of all the cars in the car yard.

  *See the screen shot provided: list_all_cars
"""


def list_all_cars():
    print('\tSell Car')
    print('----------------------\n')

    my_cars = cars.all_cars()
    print(f'Cars in yard (Total: {len(my_cars)})')

    print('NO#\tRego\tMode\tColor\tPrice')

    for i in range(0, len(my_cars)):
        print(str(i + 1) + '.' + my_cars[i].description())

def quit_car():
    print()
    print("Terminating ... ")
