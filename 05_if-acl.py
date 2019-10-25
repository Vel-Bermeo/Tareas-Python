# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:50:36 2019

@author: CEC
"""

aclnum=int(input("What is the IPv4 ACL number?: "))
if aclnum >=1 and aclnum <=99:
    print("This is a standar IPv4 ACL.")
elif aclnum >=100 and aclnum <= 199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not a standar or an extended IPv4 ACL.")
print("-----------------")
    
devices=["R1","R2","R3","S1","S2",]
for item in devices:
    print(item)
print("-----------------")
for item in devices:
    if "R" in item:
        print(item)
print("-----------------")
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
print(switches)
print("-----------------")