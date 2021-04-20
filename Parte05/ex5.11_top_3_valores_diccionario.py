# Ejercicio 5.11: Encontrar los tres valores mayores en un diccionario.

import operator
from heapq import nlargest

productos = {'Mouse': 29.9, 'Teclado': 119.9, 'Audífonos': 35.9, 'Monitor': 299}
print('Contenido actual del diccionario `productos`:', productos)

print()

# Solución 1:
print('Solución 1:')

productos_ordenados = dict(sorted(productos.items(), key=operator.itemgetter(1)))

tres_mas_caros = {}

while len(tres_mas_caros) < 3: 
    atributo = productos_ordenados.popitem()
    tres_mas_caros[atributo[0]] = atributo[1]

print('Los tres productos mas caros son:', tres_mas_caros)

# Solución 2:
print('Solución 2:')

productos_mas_caros_3 = nlargest(3, productos, key=productos.get)
print('Los tres productos mas caros son:', productos_mas_caros_3)