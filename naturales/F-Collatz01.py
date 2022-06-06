# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 20:59:33 2021
Forma normalizada (eje y)
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
    r = list(map(lambda x: x*100.0/i, SecColl(i)))
    plt.plot(r)    
plt.show()

# Hay que revisar funcionamiento Plot