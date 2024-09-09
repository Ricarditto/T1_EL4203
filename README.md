# T1 EL4203 Ricardo Salas Espiñeira
## Preguntas teóricas

1. ¿Qué es un paradigma de programación?

    **R:** Un paradigma de programación es una forma de organizar y razonar sobre los programas. Un ejemplo de esto es la programación orientada objetos.

2. ¿En qué se basa la programación orientada a objetos?

    **R:** La programación orientada a objetos permite crear instancias de clases, llamadas objetos. Las clases definen atributos y métodos que los objetos pueden tener. La creación de programas involucra la creación de objetos y la interacción entre ellos.

3. ¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación big 𝑂?

    **R:** Una función se dice recursiva si la función se llama a si misma de forma directa o indirecta. Esto permite dividir el problema en otros más pequeños y de menor complejidad. Por otro lado, las funciones iterativas presentan una secuencia de instrucciones que se repiten varias veces, generalmente mediante el uso de bucles como `for` y `while`. Un mismo problema puede ser resuelto de forma iterativa o recursiva. Se puede saber que implementación es más eficiente en terminos de su complejidad mediante la notación big O. Por lo general la iteración tiene una complejidad O(n), donde n es la cantidad de veces que se realiza el bucle. Por otra parte, la recursividad tiene una complejidad que depende del problema y del algoritmo que se utilice para resolver dicho problema. 
    
    Por ejemplo, si se busca encontrar el máximo valor dentro de un arreglo de largo n, una solución iterativa deberá recorrer todo el arreglo, lo cual presenta una complejidad O(n). Implementar el algoritmo recursivo de dividir para reinar permite solucionar este problema en tiempo O(log(n)). 

    En contraparte, si queremos calcular la serie de Fibonacci, una solución recursiva tendría una complejidad de O(n^2), mientras que la iterariva O(n).

4. Explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)

    **R:** La notación O(1) representa una complejidad constante, por lo que el tiempo de ejecución de un algoritmo no depende del tamaño de la entrada. Este es un rendimiento ideal para un algoritmo, puesto que aumentar el tamaño de la entrada no perjudica el tiempo de ejecución. Por otro lado, la notación O(n) representa complejidad lineal, donde el tiempo de ejecución del algoritmo aumenta linealmente con el tamaño de la entrada. O(1) presenta un mejor rendimiento que O(n).

5. ¿Cómo se calcula el orden en un programa que funciona por etapas?
    
    **R:** Se debe calcular la complejidad de cada etapa. La complejidad del programa será la complejidad de la etapa dominante, es decir, aquella que sea más costosa (más compleja).


6. ¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?

    **R:** Se debe definir la ecuación de recurrencia del algoritmo. Esta se construye a partir del caso base (por lo general de complejidad constante) y los subproblemas. Luego, se debe resolver la ecuación utilizando el teorema maestro.
