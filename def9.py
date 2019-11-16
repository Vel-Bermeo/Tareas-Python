# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:17:49 2019

@author: CEC
"""

def createList(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))