import matplotlib.pyplot as plt

def Coll(n): # Función Collatz
    if n%2 == 0: return n//2
    else: return 3*n + 1

n = int(input("Entrar un número natural: "))
s = [] # Contenedor de la secuencia
while n != 1: # Repetir mientras n sea diferente de 1
    s.append(n)
    n = Coll(n)
s.append(1)
plt.plot(s) # Dibujar la secuencia
plt.show() # Mostrar el dibujo
