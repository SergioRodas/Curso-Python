# Ejercicio 1. Capturar la temperatura (sea en grados Celcius o Fahrenheit) y convertirla a la escala contraria.

# 100ºC, 100ºF

captura = input('Ingrese la temperatura que desea convertir (e.g., 100ºC, 32ºF): ')

escala = captura[-2:].lower()

if escala == 'ºc':
    valor = float(captura[:-2])
    fahrenheit = valor * 1.8 + 32
    print('{}º Celcius es equivalente a {}º Fahrenheit.'.format(valor, fahrenheit))
elif escala == 'ºf':
    valor = float(captura[:-2])
    celcius = (valor - 32) / 1.8
    print('{}º Fahrenheit es equivalente a {}º Celcius.'.format(valor, celcius))
else:
    print('Debe indicar la temperatura con el siguiente formato `100ºF`, `100ºC`. Por favor vuelva a intentarlo.')
    