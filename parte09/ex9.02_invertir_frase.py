# Ejercicio 9.2: Capturar una palabra o frase del usuario e invertirla.

frase = input('Escriba una frase o palabra: ')

print('La frase original es:', frase)

frase_invertida = ''

for letra in frase:
    frase_invertida = letra + frase_invertida

print('La frase invertida es:', frase_invertida)
