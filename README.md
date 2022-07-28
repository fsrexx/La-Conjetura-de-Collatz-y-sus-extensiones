# La Conjetura de Collatz y sus extensiones
 Aplicaciones escritas en Python

## Introducción
La Conjetura de Collatz se plantea en el conjunto de los números naturales $\N=\{1, 2, 3, ...\}$ de forma muy simple:  
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

**Grafos de Collatz**

Las secuencias de Collatz pueden verse como ramas (conjunto conectado de vértices mediante aristas) de un grafo dirigido, donde el vértice origen de cada arista tiene la etiqueta n y el vértice destino tiene la etiqueta C(n), siendo C(n) el resultado de la función de Collatz. Por lo tanto, el conjunto de ramas da lugar a un grafo que representa todas las secuencias.
Retomando el programa Coll-00.py y utilizando el módulo Digraph de la biblioteca graphviz podemos construir el programa G-Coll-00.py (incluido en la carpeta "naturales").

En la función GrColl(n, aristas) se construye el grafo, para ello se crea un contenedor de vértices “s” en el que se incluyen los nuevos vértices sin repetirlos. Para evitar las repeticiones usamos la función “n not in s” vista anteriormente. Las aristas se construyen uniendo el vértice origen con el vértice destino (antes y después de aplicar la función de Collatz). Hay dos bucles, el exterior para fabricar todas las secuencias (de 1 a n) y el interior para cada secuencia (la parte que aún no se ha incluido en secuencias anteriores).
Es importante observar que la función “GrColl” devuelve el parámetro “aristas” modificado, ya que al tratarse de una lista es un parámetro mutable. Por dicho motio no se requiere una instrucción “return”.
El grafo obtenido se guarda en un archivo png temporal que se muestra en una ventana usando la opción “view = True”.

Para n = 7:

![Grafo de Collatz para n=7](imagenes/G-Collatz-7.png)

Los grafos obtenidos de esta forma son muy asimétricos. Utilizando la relación inversa de Collatz se pueden obtener grafos con un aspecto mucho más simétrico haciendo crecer las ramas de manera uniforme.

**Collatz inverso**

La relación inversa de Collatz no es unívoca, puede dar lugar a uno o dos valores según el tipo de vértices que estemos analizando. Por ejemplo, en el grafo anterior el vértice 10 da lugar a los valores 3 (3·3+1 = 10) y 20 (20/2 = 10), mientras que 3 solo da lugar a 6 (6/2 = 3) ya que x·3 + 1 = 3 implica x = 2/3 que no es un número natural.  
Si consideramos tres vértices del grafo (a, b, c) conectados de la siguiente forma: a→c,b→c es evidente que si “a” es par, “b” debe ser impar, y al contrario ( si “a” es impar, “b” debe ser par). Tomemos el primer caso (“a” par), para que estos tres vértices existan se debería cumplir: “a = 2·c” y “b = (c – 1)/3”, pero para un “c” arbitrario no siempre existirá un valor “b” que cumpla esta condición y que sea impar. En conclusión “a” siempre existe y “b”, dependiendo del valor de “c”, puede existir o no. Evidentemente el mismo razonamiento vale para para el caso “a” impar (intercambiando los papeles de “a” y “b” en el razonamiento anterior).  
La condición (c – 1)/3 entero equivale a “c%3 = 1” y la condición “[(c – 1)/3]%2 = 1” (impar) equivale a “c%2 = 0” cuando existe (c – 1)/3 entero (es decir c%3 = 1). Las condiciones “c%3 = 1” y “c%2 = 0” conjuntamente equivalen a “c%6 = 4”. Tabla explicativa:

| Módulo | resto | resto | resto | resto | resto | resto |
| -- | -- | -- | -- | -- | -- | -- |
| %3 | 0 | 1 | 2 | 0 | 1 | 2 |
| %2 | 0 | 1 | 0 | 1 | 0 | 1 |
| %6 | 0 | 1 | 2 | 3 | 4 | 5 |

$$C^{-1}(n)=\begin{cases}
\{ 2n, (n-1)/3 \} & \quad n \equiv 4 \pmod 6 \newline 
\{ 2n \} & \quad  n \not\equiv 4 \pmod 6 
\end{cases} $$

El programa G-Coll-Inv-00.py utiliza la relación inversa de Collatz y la búsqueda de vértices por el método de los niveles. El método de los niveles es adecuado para la búsqueda de vértices en un grafo con estructura de árbol. En este caso tenemos el bucle final que lo complica, pero lo hemos evitado excluyendo el vértice 1 en la búsqueda de impares y lo hemos restituido en el programa principal.

Para una profundidad d = 11:

![Grafo de Collatz para d=11](imagenes/G-Coll-Inv-11.png)

**Aspectos topológicos del Grafo de Collatz**

Como **aspecto global** podemos decir que si existe otro ciclo o alguna rama que diverge al infinito, tendremos una partición de los números naturales (una parte por cada ciclo diferente y una parte por cada rama independiente que tienda al infinito). Por lo tanto, podemos decir que la *Conjetura de Collatz es equivalente a que su grafo dirigido sea débilmente conexo* (es decir, que el grafo no dirigido subyacente sea conexo). También es equivalente a decir que *todos los números naturales se pueden obtener aplicando reiteradamente la relación inversa de Collatz*. En lenguaje matemático:
$$\forall n \in \mathbb{N}, \exists k \in \mathbb{N}: n \in C^{-k}(1)$$
De otra forma:
$$\mathbb{N}=⋃_{k∈N}C^{-k}(1)$$
Cada valor k genera un conjunto finito de números naturales que podemos interpretarlo como un nivel del grafo (distancia al elemento raíz de etiqueta 1). Estos niveles definen una partición de N. Cada elemento x del nivel k también define una partición de N (todos los elementos de los niveles inferiores a k y los generados recursivamente con la relación inversa de Collatz a partir de cada x).


Como **aspecto local** vemos que cada vértice siempre tiene una salida, una entrada par y, dependiendo de su valor (si es congruente con 4 módulo 6), puede tener una entrada impar. Pero parte de esta información puede propagarse a lo largo de algunas ramas del grafo (en sentido inverso).   
Por ejemplo, si miramos la rama que parte del vértice 3 podemos observar que carece de entradas impares (la no congruencia con 4 módulo 6 se propaga a lo largo de esta rama). Efectivamente la única entrada en el vértice 3 es 6, ya que la entrada n impar sería 3·n + 1 = 3 que no es un número entero. Pero todos los vértices de esta rama son de la forma 3·2r que son congruentes con 0 módulo 6 para r > 0 y congruente con 3 módulo 6 para r = 0, por lo tanto, no cumplen la congruencia con 4. Podemos decir que se trata de una rama “pelada” (sin bifurcaciones). Vemos que se transmite la congruencia 0 módulo 6.  
Esta situación se generaliza a todos los múltiplos de tres impares (es decir de la forma 3p, siendo p cualquier impar). Efectivamente los múltiplos de 3 no son congruentes con 4 módulo 6 (los pares son congruentes con 0 y los impares con 3) y por lo tanto no pueden dar lugar a ramas impares. Los vértices de las ramas pares son de la forma 2q3p, siendo q cualquier natural, que son congruentes con 0 módulo 6 y, por lo tanto, nunca pueden dar lugar a ramas impares. Se trata de una rama “pelada”.  
Ahora veamos lo que ocurre con los números congruentes con 1, 2 y 5 módulo 6. Como no son congruentes con 4 módulo 6 solo dan lugar a ramas pares con las siguientes secuencias inversas: (1, 2, 4), (2, 4), (5, 4). Todos terminan con valores congruentes con 4 módulo 6.  
Finalmente los números congruentes con 4 módulo 6 tienen las dos ramas, la par que sigue la alternancia inversa (2, 4, 2, 4,…) y la impar que puede ser del tipo 1, 3 o 5.


**Teorema de la rama pelada**: Vemos que el vértice de llegada de la rama pelada siempre nos da el resto 3 al dividir entre 6 y los siguientes el resto 0. Es decir que *las ramas peladas finalizan con un impar múltiplo de 3*. Las ramas peladas están formadas por vértices cuyas etiquetas tienen la propiedad de ser múltiplos de 3. Los vértices con etiquetas múltiplos de 3 pares se sitúan dentro de las ramas peladas y los múltiplos de 3 impares son final de ramas peladas (es decir que los múltiplos de 3 siempre están en ramas peladas).  
**Teorema de la alternancia de las ramas pares**: El análisis anterior da una información adicional para las otras ramas pares no peladas: Se trata de la alternancia de las bifurcaciones (cada vez que encontramos un resto 4 moviendonos en sentido inverso). Efectivamente, el resto de las ramas pares (no peladas) o con final impar de tipo 1 o 5, *presentan una alternancia de bifurcaciones* en las formas (siempre moviéndonos en sentido inverso): (1, 2, 4, 2, 4, …), (2, 4, 2, 4, …), (4, 2, 4, 2, …) o (5, 4, 2, 4, 2, …). Por ejemplo, en el caso de n = 13 tenemos: (1, 2, 4, 2, 4, …).

Si damos colores a los vértices del grafo para los restos módulo 6, tenemos para d = 12:

![Grafo de Collatz coloreado para d=12](imagenes/G-Coll-Inv-12c.png)

## Secuencias compactas

**Primera compactación: Secuencias de Terras**

Mirando la definición de la función de Collatz se observa que para n impar el resultado 3n + 1 es par, con lo que el paso siguiente sería (3n + 1)/2. Por lo tanto, se puede acortar las secuencias de Collatz con una nueva función (propuesta por Terras y también llamada función “atajo”):

$$T(n)=\begin{cases}
n/2 & \quad n \equiv 0 \pmod 2 \newline
(3n + 1)/2 & \quad n \equiv 1 \pmod 2
\end{cases}$$

Si comparamos las secuencias de Collatz y de Terras para el valor 7:  
Collatz: 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1  
Terras: 7, 11, 17, 26, 13, 20, 10, 5, 8, 4, 2, 1  
Se observa que las secuencias de Terras son subsecuencias de las secuencias de Collatz donde se conservan todos los números impares y algunos números pares.


El programa G-Terr-00.py obtiene el grafo que contiene todos los vértices con etiqueta igual o inferior al número natural n. Para n = 7:

![Grafo de Terras para n=7](imagenes/G-Terras-7.png)

En este caso (compactación de Terras) la relación inversa será:

$$T^{-1}(n)=\begin{cases}
\{ 2n, (2n-1)/3 \} & \quad n \equiv 2 \pmod 3 \newline 
\{ 2n \} & \quad  n \not\equiv 2 \pmod 3 
\end{cases} $$

El programa G-Terr-Inv-00c.py genera el grafo coloreado (con los mismos criterios que el grafo de Collatz). Para d = 9:

![Grafo de Terras coloreado para d = 9](imagenes/G-Terras-Inv-9c.png)

Se observa el cambio de los vértices con bifurcación en las ramas pares (en lugar de los vértices tipo 4, se bifurca en los de tipo 2) y en los vértices de tipo 5.

**Segunda compactación: Secuencias de Siracusa**

Una compactación más fuerte es la aplicación de Siracusa, que reemplaza el valor $3n + 1$ de la función de Collatz por $(3n + 1)/2^k$ siendo k la potencia de 2 más alta que divide a $3n + 1$. De esta forma la función resultante es una aplicación de los números impares en los números impares:  
$C(2\mathbb{N})→C(2\mathbb{N})$ Siendo $C(2\mathbb{N})$ el conjunto complementario de $2\mathbb{N}$ en $\mathbb{N}$. También se puede escribir $C(2\mathbb{N})=2\mathbb{N}-1$ para $\mathbb{N}=\{1,2,3,…\}$:

$$S(n)=\frac{3n+1}{2^k}$$

La aplicación reiterada de esta función a un determinado número impar nos produce la secuencia de Siracusa, equivalente a la secuencia de Collatz donde se han omitido todos los números pares. *La conjetura de Collatz es equivalente a la existencia de un número q tal que para cualquier número n impar se verifica:* $S^q (n)=1$