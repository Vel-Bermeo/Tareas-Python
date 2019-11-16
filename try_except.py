# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:34:32 2019

@author: CEC
"""

try:
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You can not divide by zero, sorry")
except ValueError:
    print("You must enter an integer value")
except:
    print("Oh dear, something went wrong...")
print("THE END")