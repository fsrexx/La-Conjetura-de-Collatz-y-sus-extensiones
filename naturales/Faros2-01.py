# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:43:03 2021
Faros tipo 2 (primer vértice inferior al inicial)
@author: fabio
"""

import matplotlib.pyplot as plt

def Coll(n): # Función Collatz
    if n%2 == 0: return n//2
    else: return 3*n + 1
    
n = int(input("Entrar un número entero: "))

cpv = [] # Contenedor de primer vértice inferior al inicio
for m in range(1,n+1): # Secuencias desde m = 1 a m = n (ambos incluidos)
    pv = 1
    q = m
    while q != 1: # Repetir mientras m sea diferente de 1 (secuencia de q)
        if q < m: # primer q < m
            pv = q
            break
        # mx = max(mx, q) # Calcula el máximo de la secuencia
        q = Coll(q)
    cpv.append(pv) # Añade el máximo al contenedor
plt.plot(cpv, "ro") # Dibujar los máximos
plt.show() # Mostrar el dibujo