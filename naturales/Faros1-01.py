# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:55:38 2021
Representación de los números faros tipo 1
@author: fabio
"""

import matplotlib.pyplot as plt

def Coll(n): # Función Collatz
    if n%2 == 0: return n//2
    else: return 3*n + 1
    
n = int(input("Entrar un número entero: "))

cmx = [] # Contenedor de máximos
for m in range(1,n+1): # Secuencias desde m = 1 a m = n (ambos incluidos)
    mx = q = m
    while q != 1: # Repetir mientras m sea diferente de 1 (secuencia de q)
        mx = max(mx, q) # Calcula el máximo de la secuencia
        q = Coll(q)
    cmx.append(mx) # Añade el máximo al contenedor
plt.plot(cmx, "ro") # Dibujar los máximos
plt.show() # Mostrar el dibujo