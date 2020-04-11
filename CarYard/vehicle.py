# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:28:58 2019

@author: upoudel
"""

"""  
   Task 10:  Complete the implementation of a Car class. It should include: 
             -Instance variables/attributes:  rego,model, color,price 
             -Constructor with parameters corresponding to all the instance vaiables
             -description() method that returns the details of a Car instance (rego,model, color,price)suitable for display


   Task 11:  Designs an UML model of the Car class in your report

"""


class Car:
    def __init__(self, rego, model, color, price):
        self.rego = rego
        self.model = model
        self.color = color
        self.price = price

    def description(self):
        return ' \t' + self.rego + ' \t' + self.model + ' \t' + self.color + ' \t$' + str(self.price)
