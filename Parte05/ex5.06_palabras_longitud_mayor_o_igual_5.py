# Ejercicio 5.6: Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.

colores = ['Rosa', 'Rojo', 'Verde', 'Violeta', 'Azul', 'Amarillo', 'Blanco', 'Celeste', 'Marrón']
print('Colores:', colores)
print('Cantidad actual de colores:', len(colores))

print()

# Solución 1:
print('Solución 1:')
colores_mas_largos = []
for c in colores:
    if len(c) > 4:
        colores_mas_largos.append(c)

print('Colores con al menos 5 caracteres de longitud:', colores_mas_largos)
print('Cantidad actual de colores:', len(colores_mas_largos))

print()

# Solución 2:
print('Solución 2:')

colores_mas_largos = [c for c in colores if len(c)>4]

print('Colores con al menos 5 caracteres de longitud:', colores_mas_largos)
print('Cantidad actual de colores:', len(colores_mas_largos))