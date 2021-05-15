# Ejercicio 11.9: Crear una función recursiva para comprobar si una cadena es palíndromo.

def es_palindromo(cadena):
    """
    Determina si una palabra es palíndromo.

    Parameters:
    cadena: Cadena de caracteres sobre la que se realiza la comprobación.

    Returns:
    True si la cadena es palíndromo, False en caso contrario.
    """
    if len(cadena) < 1:
        return True
    else:
        if cadena[0] == cadena[-1]:
            return es_palindromo(cadena[1:-1])
        else:
            return False

print('¿oso es palíndromo?:', es_palindromo('oso'))
print('¿neuquen es palíndromo?:', es_palindromo('neuquen'))
print('perro es palíndromo?:', es_palindromo('perro'))