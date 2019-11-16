# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:25:40 2019

@author: CEC
"""

def es_primo(numero):
  
    for i in range(2,numero):
        if (numero%i)==0:
            return False
    return True
 
numero = int(input("inserta un numero: "))
if numero==0 or numero==1:
    print ("\nEl numero NO es primo")
elif es_primo(numero):
   print ("\nEl numero es primo")
   for bi in range(1, numero):
       if es_primo(bi + 1):
           print(bi + 1, end=" ")
   print()
else:
    print ("\nEl numero NO es primo")
    for bi in range(1, numero):
       if es_primo(bi + 1):
           print(bi + 1, end=" ")
    print()


    

