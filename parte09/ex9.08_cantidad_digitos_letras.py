# Ejercicio 9.8: Contar la cantidad de dígitos y letras que tiene un texto.

# SOLUCIÓN:

texto = input('Ingrese un texto: ')

letras = []
digitos = []

for i in texto:
    if i.isdigit():
        digitos.append(i)
    elif i.isalpha():
        letras.append(i)

print('Cantidad de letras en el texto:', len(letras))
print('Cantidad de dígitos en el texto:', len(digitos))