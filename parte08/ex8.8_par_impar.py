# Ejercicio 8. Determinar si un número dado por el usuario es par o impar.

print('Bienvenido, le diremos si el numero elegido es par o impar.')

numero = int(input('Por favor digite un número entero: '))

if numero % 2 == 0:
    print('El número {} es par.'.format(numero))
else:
    print('El número {} es impar.'.format(numero))
    