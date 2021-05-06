# Ejercicio 9.4: Calcular el factorial de un número dado por el usuario.

# Solución:

# 0! = 1
# 1! = 1

# 5! =  1 * 2 * 3 * 4 * 5 = 120
# 6! = 720

numero = int(input('Por favor ingrese un número entero positivo: '))

if numero >= 0:
    i = 0
    factorial = 1
    while i < numero:
        factorial = factorial * (i+1)
        i += 1
    print('EL factorial de {} es {}.'.format(numero, factorial))
else:
    print('El numero ingresado es incorrecto. Inténtelo de nuevo.')