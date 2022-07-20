# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:13:54 2021
Grafo de Terras
@author: fabio
"""

from graphviz import Digraph as dg

def Terr(n): # Función Terras
    if n%2 == 0: return n//2
    else: return (3*n + 1)//2
    
def GrTerr(n, aristas): # Grafo de Terras
    s = [] # Contenedor de los vértices del grafo
    for m in range(1, n+1): # Analiza todas las secuencias (de 1 a n)       
        while m not in s: # Hasta encontrar un vértice previo
            ma = m # vértice origen
            s.append(m)
            m = Terr(m) # vértice destino
            aristas([(str(ma),str(m))]) # Arista ma-m

n = int(input("Entrar un número natural: "))

g = dg(name = "Terras")
GrTerr(n, g.edges)
g.format = "png"
g.render(view = True)