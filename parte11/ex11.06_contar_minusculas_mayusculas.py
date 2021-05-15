# Ejercicio 11.6: Usar una función para contar minúsculas y mayúsculas en una cadena.

def contar_minusculas_mayusculas(cadena): 
    """
    Cuenta la cantidad de minúsculas y mayúsculas que hay en una cadena de caracteres.

    Parameters:
    cadena: Cadena de caracteres con el texto.

    Returns:
    Tupla con la cantidad de minúsculas y mayúsculas
    """

    if cadena:
        if isinstance(cadena, str):
            mayusculas = 0
            minusculas = 0
            for c in cadena:
                if c.islower():
                    minusculas += 1
                elif c.isupper():
                    mayusculas += 1

            return minusculas, mayusculas
        else:
            raise TypeError('El argumento ingresado no es válido. Por favor ingrese una cadena de caracteres.')
    else:
        print('No has proveído datos. Por favor ingrese una cadena de caracteres como argumento.')

frase = 'Mi abuela Patea CAlefones.'

try:
    resultado = contar_minusculas_mayusculas(frase)
    print('La frase es: "{}"'.format(frase))
    print('La cantidad de minúsculas es: {}. La cantidad de mayúsculas es: {}.'.format(resultado[0], resultado[1]))
except TypeError as e:
    print('ERROR:', e)

print()

frase = 8

try:
    resultado = contar_minusculas_mayusculas(frase)
    print('La frase es: "{}"'.format(frase))
    print('La cantidad de minúsculas es: {}. La cantidad de mayúsculas es: {}.'.format(resultado[0], resultado[1]))
except TypeError as e:
    print('ERROR:', e)

print()

frase = 'sergio'

try:
    resultado = contar_minusculas_mayusculas(frase)
    if resultado:
        print('La frase es: "{}"'.format(frase))
        print('La cantidad de minúsculas es: {}. La cantidad de mayúsculas es: {}.'.format(resultado[0], resultado[1]))
except TypeError as e:
    print('ERROR:', e)