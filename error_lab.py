# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:49:21 2019

@author: CEC
"""

def readint(prompt, mini, maxi):
    while True:
        try: 
            x=int(input("Ingrese el valor: "))
            
            if x<maxi and x>mini:
                break
            else:
                1/0
        except ValueError:
            print("Error: wrong input ")
        except ZeroDivisionError:
            print("Error: the value is not within permitted range (-10..10) ")
    return x
    
#

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)