# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:10:22 2019

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
# your code from LAB 4.1.3.6
#

def daysInMonth(year, month):
#    meses={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#    if isYearLeap(year)== True:
#        return meses[month]
#    elif meses[2]==28:
#        return meses[month]
#    else:
#        return None
# put your new code here
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res
print(daysInMonth(2019,10))
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
