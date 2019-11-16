# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:35:37 2019

@author: CEC
"""
from math import pi,radians,degrees,sin,cos,tan,asin,e,exp,log,ceil,floor,trunc
import datetime
from platform import machine

Time=datetime.datetime.now()
print(Time.isoformat())

ad=90
ar=radians(ad)
ad=degrees(ar)

print(ad==90.)
print(ar==pi/2.)
print(sin(ar)/cos(ar)==tan(ar))
print(asin(sin(ar))==ar)

print(pow(e,1)==exp(log(e)))
print(pow(e,1)==exp(2*log(2)))
print(pow(e,1)==exp(0))

x=1.4
y=2.6
print(floor(x),ceil(y))
print(trunc(-x),ceil(y))

print(machine())