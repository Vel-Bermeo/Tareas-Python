# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:25:00 2019

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
print(json_data)