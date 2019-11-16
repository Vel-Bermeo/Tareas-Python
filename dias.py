# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:48:54 2019

@author: CEC
"""

def isYearLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            return False
        return True
    else:
        return False
#
# Su codigo AQUI
#
# your code from LAB 1
#

def daysInMonth(year, month):
     if year < 1582 or month < 1 or month > 12:
        return None
     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     res  = days[month - 1]
     if month == 2 and isYearLeap(year):
        res = 29
     return res
#
# your code from LAB 2
#

def dayOfYear(year, month, day):
    if day < 1 or day > 31:
        return None
    #isYearLeap(year)
    #daysInMonth(year, month)
    daysInMonth(year, month)
    
#
# put your new code here
#

print(dayOfYear(2004, 12, 31))
#if isYearLeap(year)==True:
#    print('El año tiene 366 días')
#else:
#    print('El año tiene 365 días')

