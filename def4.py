# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:50:23 2019

@author: CEC
"""

def address(street,city,postalCode):
    print('Your address is:',street,'St.',city,postalCode)

a=input('Street: ')
pc=input('Postal Code: ')
c=input('City: ')

address(a,c,pc)
