# Ejercicio 9. Comprobar si un número es capicúa.

print('¿Es capicúa o no?')

numero = int(input('Por favor digite un número entero positivo: '))
numero_al_reves = int(str(numero)[::-1])
if numero >= 0:
    if numero == numero_al_reves:
        print('El número {} es capicúa.'.format(numero))
    else:
        print('El número {} no es capicúa.'.format(numero))
else:
    print('El número debe ser positivo.')