# Ejercicio 9.10: Realizar cálculos de estadísticas básicos: media, mínimo, máximo.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma = 0

for n in numeros:
    suma += n 

print('Suma:', suma)

media = suma / len(numeros)

print('Media:', media)

minimo = numeros[0] 

for n in numeros: 
    if n < minimo:
        minimo = n

print('Mínimo:', minimo)

maximo = numeros[0] 

for n in numeros: 
    if n > maximo:
        maximo = n

print('Máximo:', maximo)