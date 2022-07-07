# -*- coding: utf-8 -*-
"""
Created on Fri May 28 17:36:38 2021
Grafo con Collatz Inverso
@author: fabio
"""
from graphviz import Digraph as dg

def CollInv(n):
    par = 2*n # Siempre hay una entrada par
    if n%6 == 4: # Condición de existencia de rama impar
        impar = (n-1)//3        
    else: impar = None # No cumple las condiciones requeridas
    return par, impar

def LongRama(r, aristas): # Longitud de las ramas
    s = [1] # Contenedor de vértices por niveles (nivel 0)
    for i in range(r): # recorre la longitud de las ramas (por niveles)
        sn = [] # Contenedor vértices nuevo nivel
        for n in s: # explora los vértices existentes
            par, impar = CollInv(n)
            sn.append(par) # añade el vértice de la rama par
            aristas([(str(par), str(n))]) # arista par
            if (not impar is None) and (impar != 1): # Si existe rama impar
            # Se excluye el 1 para evitar el bucle
                sn.append(impar) # añade el vértice de la rama impar
                aristas([(str(impar), str(n))])
        s = sn # renovación del nivel
        
d = int(input("Entrar profundidad de la búsqueda (>3): "))

g = dg(name = "Collatz")
g.edges([("1","4")]) # Se restituye el bucle 
LongRama(d, g.edges) # Añade las aristas
g.format = "png"
g.render(view = True)
