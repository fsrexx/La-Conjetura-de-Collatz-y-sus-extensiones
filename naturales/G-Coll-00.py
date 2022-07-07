# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:34:59 2021
Grafo de Collatz
@author: fabio
"""

from graphviz import Digraph as dg

def Coll(n): # Función Collatz
    if n%2 == 0: return n//2
    else: return 3*n + 1
    
def GrColl(n, aristas): # Grafo de Collatz
    s = [] # Contenedor de los vértices del grafo
    for m in range(1, n+1): # Analiza todas las secuencias (de 1 a n)       
        while m not in s: # Hasta encontrar un vértice previo
            ma = m # vértice origen
            s.append(m)
            m = Coll(m) # vértice destino
            aristas([(str(ma),str(m))]) # Arista ma-m

n = int(input("Entrar un número natural: "))

g = dg(name = "Collatz")
GrColl(n, g.edges)
g.format = "png"
g.render(view = True)