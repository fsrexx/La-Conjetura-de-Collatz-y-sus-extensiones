# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:32:39 2021
Collatz Secuencia generada por un número entero
@author: fabio
"""

def Coll(n): # Función Collatz
    if n%2 == 0: return n//2
    else: return 3*n + 1
    
def SecColl(n): # Secuencia de Collatz
    m = n
    s = [] # Contenedor de la secuencia
    while m not in s: # Hasta encontrar el bucle
        s.append(m)
        m = Coll(m)
    return s

n = int(input("Entrar un número entero: "))
print(SecColl(n))
