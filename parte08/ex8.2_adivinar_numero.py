# Ejercicio 2. Pedir al usuario que adivine un número. Sólo un intento.

from random import randint

aleatorio = randint(1,10)

print('Adivine un número entre 1 y 10')

numero = int(input('Escriba un número: '))

if numero == aleatorio:
    print('¡Felicitaciones! Acertó, el número era {}'.format(aleatorio))
elif numero < 1 or numero > 10:
    print('Solo están permitidos números entre 1 y 10.')
else:
    print('No has acertado, el número era {}'.format(aleatorio))

