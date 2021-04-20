# Ejercicio 5.13: Realizar operaciones de unión e intersección de conjuntos.

numeros = set(list(range(1,11)))
primos = set([2, 3, 5, 7, 11, 13, 17, 19])

print('Contenido del conjunto `numeros`:', numeros)
print('Contenido del conjunto `primos`:', primos)

print()

print('Operación de unión:')
union_numeros = numeros.union(primos)
print('Contenido del conjunto `union_numeros`:', union_numeros)
print('Cantidad de elementos del conjunto `union_numeros`:', len(union_numeros))

print()

print('Operación de intersección:')
interseccion_numeros = numeros.intersection(primos)
print('Contenido del conjunto `interseccion_numeros`:', interseccion_numeros)
print('Cantidad de elementos del conjunto `interseccion_numeros`:', len(interseccion_numeros))
