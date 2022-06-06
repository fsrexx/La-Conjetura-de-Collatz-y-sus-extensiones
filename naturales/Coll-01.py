# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:13:07 2021
Collatz Secuencia generada por un número natural
(No se buscan bucles)
@author: fabio
"""

def Coll(n): # Función Collatz
    if n%2 == 0: return n//2
    else: return 3*n + 1
    
n = int(input("Entrar un número natural: "))
while n != 1: # Repetir mientras n sea diferente de 1
    print(n, end=", ") # Evitar salto de línea
    n = Coll(n)
print(1) 
   
