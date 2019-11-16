# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:45:02 2019

@author: CEC
"""

import urllib.parse
import requests

main_api="http://www.mapquestapi.com/directions/v2/route?"
orig="Quito"
dest="Piñas, El Oro"
key="prhsJxZuPH4h5esro90QuMUDdcpwd7oM"
url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})

json_data=requests.get(url).json()
print("URL: "+(url))
json_data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]

if json_status==0:
    print("API Status: " +str(json_status)+"= A successful route call.\n")