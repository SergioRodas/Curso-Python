# Ejercicio 11.4: Crear una función para invertir el contenido de una cadena de caracteres.

def invertir_cadena(texto):
    """
    Invierte una cadena de caracteres (texto).

    Parameteres:
    texto: Cadena de caracteres (texto) a invertir.

    Returns:
    Cadena de caracteres invertida.
    """

    if isinstance(texto, str):
        cadena_inversa = texto[::-1]
        return cadena_inversa
    else:
        raise TypeError('No se ha especificado una cadena de caracteres')

cadena = "Hola Mundo"

try:
    resultado = invertir_cadena(cadena)

    print('Texto original:', cadena)
    print('Texto invertido:', resultado)
except TypeError as e:
    print('Error:', e)

print()

cadena = 1000

try:
    resultado = invertir_cadena(cadena)

    print('Texto original:', cadena)
    print('Texto invertido:', resultado)
except TypeError as e:
    print('Error:', e)

print()

cadena = ['Py', 'thon']

try:
    resultado = invertir_cadena(cadena)

    print('Texto original:', cadena)
    print('Texto invertido:', resultado)
except TypeError as e:
    print('Error:', e)