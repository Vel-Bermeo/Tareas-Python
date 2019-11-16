# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:25:40 2019

@author: CEC
"""

def es_primo(numero):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
  
    for i in range(2,numero):
        if (numero%i)==0:
            return False
    return True
 
while True:
    try:
        numero = int(input("inserta un numero (0) salir >> "))
        if numero==0:
            print ("\nEl numero %s NO es primo")
            for bi in range(1, numero):
                if es_primo(bi + 1):
                    print(bi + 1, end=" ")
            print()
        if es_primo(numero):
            print ("\nEl numero %s es primo")
            for bi in range(1, numero):
                if es_primo(bi + 1):
                    print(bi + 1, end=" ")
            print()
        else:
            print ("\nEl numero %s NO es primo")
    except:
        print ("\nEl numero tiene que ser entero")


"while True:"
    

