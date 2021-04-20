# Ejercicio 5.8: Calcular la frecuencia (ocurrencias) de los elementos de una lista.

from collections import Counter

colores = ['Rojo', 'Negro', 'Blanco', 'Rojo', 'Azul', 'Verde', 'Blanco', 'Celeste', 'Violeta', 'Rojo', 'Negro']

print('Contenido actual de la lista `colores`:', colores)
print('Cantidad actual de elementos de la lista `colores`:', len(colores))

print()

# Solución 1:
print('Solución 1:')

frecuencia = {} # Diccionario
for c in colores:
    if c in frecuencia:
        frecuencia[c] += 1
    else:
        frecuencia[c] = 1

print('Contenido actual del diccionario `frecuencia`:', frecuencia)
print('Cantidad actual de elementos del diccionario  `frecuencia`:', len(frecuencia))

# Solución 2:
print('Solución 2:')

contador = Counter(colores)
print('Contenido actual de la variable `contador`:', contador)
print('Cantidad actual de elementos de la variable  `contador`:', len(contador))