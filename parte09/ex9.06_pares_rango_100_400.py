# Ejercicio 9.6: Encontrar todos los números pares que hay en el rango de 100 a 400.

#SOLUCIÓN:

print('Numeros pares del 100 al 400:')
for i in range(100, 401):
    if i % 2 == 0:
        print(i, end = ' - ')