# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 20:21:36 2021
Forma de la sucesión de Collatz
@author: fabio
"""

import matplotlib.pyplot as plt

def Collatz(n):
    m = n
    if m == 0: return m
    if m%2 == 1: m = 3*m + 1
    else: m = m//2
    return m
    
def SecColl(n):
    m = n
    s = []
    while m not in s: 
        s.append(m)
        m = Collatz(m)        
    s.append(m)
    return s

n = int(input("Entrar un número entero: "))

for i in range(1,n+1):
    plt.plot(SecColl(i))
plt.show()