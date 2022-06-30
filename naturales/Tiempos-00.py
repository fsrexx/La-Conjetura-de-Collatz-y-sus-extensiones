# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:47:23 2021
Tiempor de parada: Longitudes de las secuencias
@author: fabio
"""

import matplotlib.pyplot as plt

def Coll(n): # Función Collatz
    if n%2 == 0: return n//2
    else: return 3*n + 1
    
n = int(input("Entrar un número entero: "))

cc = [] # Contenedor de tiempos
for m in range(1,n+1): # Secuencias desde m = 1 a m = n (ambos incluidos)
    q = m
    contador = 1
    while q != 1: # Repetir mientras m sea diferente de 1 (secuencia de q)
        q = Coll(q)
        contador +=1
    cc.append(contador)
plt.plot(cc, "ro") # Dibujar los tiempos
plt.show() # Mostrar el dibujo
