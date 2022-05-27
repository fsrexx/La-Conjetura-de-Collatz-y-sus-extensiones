<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script>
# La Conjetura de Collatz y sus extensiones
 Aplicaciones escritas en Python

La Conjetura de Collatz se plantea en el conjunto de los números naturales de forma muy simple:  
Se define una función C(n) que da como resultado n/2 si n es un número par y 3·n + 1 si n es un número impar.   
Aplicando C reiteradamente a cualquier n siempre llegamos a obtener 1.  
Por ejemplo, si n = 3 obtenemos la secuencia: [3, 10, 5, 16, 8, 4, 2, 1].

En lenguaje matemático podemos escribirlo de la siguiente forma:
$$C(n)=\begin{cases}
n/2 & \quad n \equiv 0 \pmod 2 \newline
3n + 1 & \quad n \equiv 1 \pmod 2
\end{cases}$$
