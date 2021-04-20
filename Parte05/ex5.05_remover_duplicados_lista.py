# Ejercicio 5.5: Remover los valores duplicados en una lista.

colores = ['Rojo', 'Negro', 'Blanco', 'Rojo', 'Azul', 'Verde', 'Blanco', 'Celeste', 'Violeta', 'Rojo', 'Negro']
print('Contenido actual de la lista `colores`:', colores)
print('Cantidad de elementos de la lista `colores`:', len(colores))

print()

colores = list(set(colores))
print('Contenido actual de la lista `colores`:', colores)
print('Cantidad de elementos de la lista `colores`:', len(colores))