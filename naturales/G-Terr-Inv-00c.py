# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:31:54 2021
Terras Inverso
@author: fabio
"""

from graphviz import Digraph as dg

def TerrInv(n):
    par = 2*n # Siempre hay una entrada par
    if n%3 == 2: # Condición de existencia de rama impar
        impar = (2*n-1)//3        
    else: impar = None # No cumple las condiciones requeridas
    return par, impar

def Fondo(n):
    c = ["white", "aqua", "orange", "green", "red", "grey"]
    return c[n%6]

def LongRama(r, g): # Longitud de las ramas
    aristas = g.edges
    s = [1] # Contenedor de vértices por niveles (nivel 0)
    for i in range(r): # recorre la longitud de las ramas (por niveles)
        sn = [] # Contenedor vértices nuevo nivel
        for n in s: # explora los vértices existentes
            par, impar = TerrInv(n)
            sn.append(par) # añade el vértice de la rama par
            g.node(str(par), fillcolor=Fondo(par))
            aristas([(str(par), str(n))]) # arista par
            if (not impar is None) and (impar != 1): # Si existe rama impar
            # Se excluye el 1 para evitar el bucle
                sn.append(impar) # añade el vértice de la rama impar
                g.node(str(impar), fillcolor=Fondo(impar))
                aristas([(str(impar), str(n))])
        s = sn # renovación del nivel
        
d = int(input("Entrar profundidad de la búsqueda (>3): "))

g = dg(name = "Terras", node_attr={"style":"filled"})
g.node("1", fillcolor=Fondo(1))
g.node("2", fillcolor=Fondo(2))
g.edges([("1","2")]) # Se restituye el bucle 
LongRama(d, g) # Añade las aristas
g.format = "png"
g.render(view = True)
