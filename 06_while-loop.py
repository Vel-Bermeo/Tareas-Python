# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:48:40 2019

@author: CEC
"""

x=input("Enter a number to count to: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break

while True:
    a=input("Enter a number to count to: ")
    if a=='q' or a=='quit':
        break
    a=int(a)
    b=1
    while True:
        print(b)
        b=b+1
        if b>a:
            break
