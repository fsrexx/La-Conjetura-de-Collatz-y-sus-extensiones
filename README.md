# La Conjetura de Collatz y sus extensiones
 Aplicaciones escritas en Python

## Introducción
La Conjetura de Collatz se plantea en el conjunto de los números naturales $\mathbb{N}=\{1, 2, 3, ...\}$ de forma muy simple:  
Se define una función C(n) (función de Collatz) que da como resultado n/2 si n es un número par y 3·n + 1 si n es un número impar.   
**Conjetura**: *Aplicando C reiteradamente a cualquier n siempre llegamos a obtener 1.*  
Por ejemplo, si n = 3 obtenemos la secuencia: [3, 10, 5, 16, 8, 4, 2, 1].

En lenguaje matemático podemos escribirlo de la siguiente forma:
$$C(n)=\begin{cases}
n/2 & \quad n \equiv 0 \pmod 2 \newline
3n + 1 & \quad n \equiv 1 \pmod 2
\end{cases}$$
Donde $a \equiv b \pmod c$ se lee: "a es congruente con b módulo c". 
Esto significa que "a" y "b" dan el mismo resto cuando se realiza su división entera euclídea entre "c". 
Es frecuente utilizar el valor del resto como valor de "b" en esta expresión. 
En este caso, en la programación de esta fórmula, también es frecuente utilizar la expresión "b = a % c", que se lee: "b es el resto de la división entera de a entre c".

## Generalidades
En la carpeta "naturales" se encuentran los programas Coll-00 y Coll-01 que generan las secuencias de Collatz de n (siendo n el número natural que se entra al solicitarlo el programa). 
Comentarios a las diferencias entre ambos programas:
- En Coll-01 se supone cierta la Conjetura de Collatz y por eso se finaliza la búsqueda cuando se obtiene el valor 1.
- En Coll-00 la búsqueda finaliza cuando se entra en un ciclo (valores que se repiten indefinidamente). Teoricamente funciona aunque no sea cierta la Conjetura de Collatz. El número 1 forma parte del ciclo: $\langle 4, 2, 1 \rangle$.
- El programa Coll-00 es extensible a lo números enteros, pero tanto para los números negativos como para el número 0 tiene otros ciclos terminales diferentes de $\langle 4, 2, 1 \rangle$. Este aspecto lo veremos con más detalle en la extensión a los números enteros.

## Ciclos
Las sucesiones de números naturales generadas por la aplicación reiterada de la función C(n) puede comportarse de dos formas:
- Entrando en un ciclo que se repite de forma indefinida. Caso del ciclo $\langle 4, 2, 1 \rangle$ (también llamado ciclo trivial).
- No repitiendo nunca ningún número, lo que conduce a la producción de números muy grandes. Divergencia.

La Conjetura de Collatz equivale a decir que no hay divergencias y que siempre terminamos en el ciclo $\langle 4, 2, 1 \rangle$.
Por lo tanto, una forma de demostrar que la Conjetura no es cierta sería encontrar un contraejemplo. Es decir encontrar otro ciclo diferente del trivial o encontrar una sucesión divergente.  
Para demostrar la inexistencia de ciclos diferentes del trivial se pueden seguir diferentes estrategias. La más directa es clasificar los ciclos por su longitud y demostrar que no existen ciclos de longitud s para cualquier valor de s.

**Propiedades de los ciclos**: 
1. *Estabilidad*: Dado un ciclo $\mathcal{C} = \langle a_1, a_2, ..., a_s \rangle$, si le aplicamos la función de Collatz obtenemos 
$\langle a_2, a_3, ..., a_s, a_1 \rangle$ que contiene los mismos elementos que el ciclo anterior. A esta propiedad se le llama estabilidad de la función de Collatz respecto a los ciclos.
2. *Relación entre pares e impares*: Sea $(b_1, b_2, ...,b_p)$ la lista de elementos pares y 
$(c_1, c_2, ..., c_q)$ la lista de elementos impares, con 
$s=p+q$. 
Si escribimos la lista completa 
$(b_1, ..., b_p, c_1, ..., c_q)$ 
vemos que no es más que un reordenamiento de 
$\mathcal{C}$. 
Aplicandole la función de Collatz tenemos 
$(b_1/2, ..., b_p/2, 3c_1 +1, ..., 3c_q +1)$
, que sigue teniendo los mismos elementos que 
$\mathcal{C}$. Por último, si cálculamos el producto de todos los elementos del ciclo 
$b_1 ... b_p c_1 ... c_q = \frac{b_1}{2} ... \frac{b_p}{2} (3c_1 +1) ... (3c_q +1)$ y simplificando: 
$$2^p=\left( 3+\frac{1}{c_1}\right) ... \left( 3+\frac{1}{c_q}\right)$$

**Ciclos de pequeña longitud**:

Para n=1 la fórmula anterior no es compatible. Debe cumplirse: 0 < p < s  
Para n=2 la fórmula anterior no es compatible. Por la misma razón.   
Para n=3 es compatible con p=2 y q=1 [$2^2=(3+1/1)$], que coincide con el ciclo trivial $\langle 4, 2, 1 \rangle$.  
Para n=4 con p=1 es incompatible ya que $2 < (3 + ...)(3 + ...)(3 + ...)$  
Para n=4 con p=2 es incompatible ya que $2^2 < (3 + ...)(3 + ...)$  
Para n=4 con p=3 es incompatible ya que $2^3 > (3 + 1/r)$ para cualquier r natural.  
Para n=5 partiremos del ciclo escrito con $a_1$ como elemento mínimo y, por lo tanto, impar. Con esto tenemos $a_2=3a_1 + 1$, que será par, y $a_3=a_4/2$. Si $a_3$ fuera par $a_4=a_3/2=a_2/4=(3a_1 +1)/4$ que implica $a_4 < a_1$ que contradice que $a_1$ sea el mínimo. Por lo tanto, $a_3$ debe ser impar y $a_4=3a_3 +1$ será par, con lo que $a_5=a_4/2$. Vemos que $a_5$ debe ser par, ya que $a_1<a_5$, por ser $a_1$ el mínimo, lo que solo es posible con $a_1=a_5/2$.
Finalmente el producto de todos los elementos del ciclo tendrá la forma: $a_1 a_2 a_3 a_4 a_5 =\frac{a_5}{2} (3a_1 +1)\frac{a_2}{2} (3a_3 +1) \frac{a_4}{2}$, que simplificando queda: $8=(3+\frac{1}{a_1})(3+\frac{1}{a_3})$, pero esta condición no se puede cumplir con $a_1$ y $a_3$ naturales, ya que 8 < (3 + ...)(3 + ...). Por lo tanto, no existen ciclos de longitud 5.  
Sin embargo, sí es compatible con los enteros negativos, donde existe un ciclo de longitud 5 tal y como veremos en el apartado dedicado a las extensiones.

## Representaciones
**Representación directa de las secuencias de Collatz**

Partiendo del programa Coll-01.py y añadiendole el módulo PyPlot de la biblioteca MatplotLib, para dibujar las secuencias de Collatz en lugar de imprimirlas, tenemos el programa F-Coll-01.py con las siguientes salidas:

Para n = 7:

![Secuencia para n=7](imagenes/S-Coll-01-n7.png)

Para n = 27:

![Secuencia para n=27](imagenes/S-Coll-01-n27.png)

Se observa un comportamiento de bruscas subidas y bajadas, lo que se conoce con el nombre de trayectoria de granizo (similar a lo que les ocurre a las gotas de granizo en el interior de las nubes).  
Estas trayectorias (representaciones gráficas de las secuencias) están enmarcadas por dos valores: Valor máximo (ordenadas) y número de iteraciones para alcanzar el valor 1 (abscisas). Ambas variables tienen comportamientos peculiares.

**Valores máximos de las secuencias**

Llamaremos faros tipo 1 a estos números, ya que parecen delimitar (acotar) el terreno en el que mueven estas secuencias. Luego veremos otros delimitadores (faros de diferentes tipos) que también acotan diferentes parámetros característicos de estas secuencias.  
El programa Faros1-01.py hace un barrido de las secuencias de 1 a n y guarda los máximos para proceder a dibujarlos.

Para n = 400:

![Faros del tipo 1 para n=400](imagenes/Faros1-n400.png)

Para n = 400 se observan agrupaciones de puntos en líneas horizontales (13.120, 9.232, 4.372, …) y en líneas inclinadas (y = x, y = 3x + 1, …). Sugiere la existencia de algo parecido a un espectro (algo que se obtiene mediante una transformación del conjunto de secuencias).

Llamaremos Faros tipo 2 a los primeros valores de la secuencia que son inferiores al valor inicial. La existencia de estos valores es equivalente a la no divergencia de la secuencia.  
El programa Faros2-01.py hace un barrido de las secuencias de 1 a n y guarda estos valores para proceder a dibujarlos.

Para n = 1000:

![Faros del tipo 2 para n=1000](imagenes/Faros2-n1000.png)

**Números de iteraciones**

La longitud de la secuencia o número de iteraciones hasta obtener el valor 1, también se conoce con el nombre de tiempo de parada (stopping time). Parece tener una cota superior que crece muy lentamente y que se dispersa progresivamente. La Conjetura de Collatz es también equivalente a decir que *cualquier entero superior a 1 tiene un tiempo de parada finito*.  
El programa Tiempos-00.py calcula estos valores haciendo un barrido de 1 a n.

Para n = 20.000:

![Tiempos de parada para n=20000](imagenes/Tiempos-n20000.png)

También es interesante ver el comportamiento del tiempo hasta llegar a los diferentes Faros.  
El tiempo para llegar a los Faros de tipo 1 se reduce notablemente respecto a los tiempos de parada (ver el programa TienposF1-00.py).

Para n = 20.000:

![Tiempos de parada para n=20000](imagenes/TiemposF1-n20000.png)

El tiempo para llegar a los Faros de tipo 2 vuelve a reducirse. 

Para n = 20.000:

![Tiempos de parada para n=20000](imagenes/TiemposF2-n20000.png)

Este efecto parece paradójico, ya que las reducciones antes de alcanzar el máximo parecen indicar que el máximo se consigue después de haber bajado del valor inicial. Es decir, primero hay bajadas o subidas seguidas de bajadas hasta valores inferiores al valor inicial y posteriormente nuevas subidas hasta alcanzar el máximo. Pero, si estos máximos se obtienen en valores inferiores al valor inicial actual, parece lógico pensar que deberían estar en la gráfica para valores iniciales anteriores. Sin embargo este "parece" no es real ya que no estamos mirando los máximos sino los valores del Faro de tipo 2.  
En resumen, parece que hay la posibilidad de encontrar un argumento recursivo que nos conduzca a encontrar una función límite de los tiempos de los diferentes Faros.
