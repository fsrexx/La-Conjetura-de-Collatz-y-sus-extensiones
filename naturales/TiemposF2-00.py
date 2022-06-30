# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 17:06:50 2022
Tiempos hasta el Faro 1
@author: fabio
"""

import matplotlib.pyplot as plt

def Coll(n): # Función Collatz
    if n%2 == 0: return n//2
    else: return 3*n + 1
    
n = int(input("Entrar un número entero: "))

cc = [] # Contenedor de tiempos hasta F2
for m in range(1,n+1): # Secuencias desde m = 1 a m = n (ambos incluidos)
    pv = 1
    q = m
    contador = cpv = 1
    while q != 1: # Repetir mientras m sea diferente de 1 (secuencia de q)
        if q > m: # primer q < m
            pv = q
            cpv = contador
            break
        q = Coll(q)
        contador +=1
    cc.append(cpv)
plt.plot(cc, "ro") # Dibujar los tiempos
plt.show() # Mostrar el dibujo