<<<<<<< HEAD
# TP — Visualización de algoritmos de ordenamiento
#README
Descripción del Proyecto

Este proyecto implementa tres algoritmos clásicos de ordenamiento en Python:

· Bubble Sort
· Insertion Sort
· Selection Sort

Cada algoritmo está adaptado para ejecutarse paso a paso, permitiendo 
visualizar en tiempo real cómo se realizan las comparaciones e intercambios entre elementos.

---
Integrantes del Equipo

· Alejandro Peralta
. Aylen Melgarejo
· Lautaro Long

---

Notas de Implementación


# Requisitos y entorno
- Python 3.10+  
- Navegador moderno (Chrome, Firefox o Edge)

Bubble Sort

· Se utiliza un enfoque por pasos controlado por las variables i (pasada actual) y j (posición de comparación).
· En cada paso se comparan items[j] e items[j+1], intercambiándolos si están en desorden.
· Dificultad principal: Estructuración del código y ubicación de instrucciones. Ademas de adaptar el algoritmo tradicional a una versión paso a paso para la visualización.

Insertion Sort

· Se usan las variables i (elemento a insertar) y j (posición actual en la sublista ordenada).
· En cada paso, el elemento en i se compara y desplaza hacia la izquierda hasta encontrar su posición correcta.
· Dificultad: Reconocer como se debe modificar las variables, que representaba exactamente cada una y errores minimos de notacion que no permitian funcionar el codigo

Selection Sort

· Se divide en dos fases: "buscar" (encontrar el mínimo) y "swap" (intercambiar).
· Variables clave: i (inicio de la sublista no ordenada), j (cursor de búsqueda), min_idx (índice del mínimo actual).
=======
# TP — Visualización de algoritmos de ordenamiento
#README
Descripción del Proyecto

Este proyecto implementa tres algoritmos clásicos de ordenamiento en Python:

· Bubble Sort
· Insertion Sort
· Selection Sort

Cada algoritmo está adaptado para ejecutarse paso a paso, permitiendo 
visualizar en tiempo real cómo se realizan las comparaciones e intercambios entre elementos.

---
Integrantes del Equipo

· Alejandro Peralta
. Aylen Melgarejo
· Lautaro Long

---

Notas de Implementación


# Requisitos y entorno
- Python 3.10+  
- Navegador moderno (Chrome, Firefox o Edge)

Bubble Sort

· Se utiliza un enfoque por pasos controlado por las variables i (pasada actual) y j (posición de comparación).
· En cada paso se comparan items[j] e items[j+1], intercambiándolos si están en desorden.
· Dificultad principal: Estructuración del código y ubicación de instrucciones. Ademas de adaptar el algoritmo tradicional a una versión paso a paso para la visualización.

Insertion Sort

· Se usan las variables i (elemento a insertar) y j (posición actual en la sublista ordenada).
· En cada paso, el elemento en i se compara y desplaza hacia la izquierda hasta encontrar su posición correcta.
· Dificultad: Reconocer como se debe modificar las variables, que representaba exactamente cada una y errores minimos de notacion que no permitian funcionar el codigo

Selection Sort

· Se divide en dos fases: "buscar" (encontrar el mínimo) y "swap" (intercambiar).
· Variables clave: i (inicio de la sublista no ordenada), j (cursor de búsqueda), min_idx (índice del mínimo actual).
>>>>>>> b05280764580393c482d218f15fc11f7963c7983
· Dificultad: sincronizar el cambio de fase y actualizar correctamente los índices después de cada intercambio.