# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:44:14 2019

@author: CEC
"""

try:
    y=1/0.2
except ZeroDivisionError:
    print("Division zero!")
except ArithmeticError:
    print("Arithmetic Problem!")

print("THE END")