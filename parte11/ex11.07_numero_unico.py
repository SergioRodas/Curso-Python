# Ejercicio 11.7: Tomar una lista de números e identificar los números únicos.

def numeros_unicos(numeros):
    """
    Obtiene los números únicos en una tupla o lista.

    Parameters:
    numeros: Lista o tupla con números.

    Returns: 
    Lista con los valores únicos.
    """
    if numeros:
        if isinstance(numeros, (list, tuple)):
            unicos = []
            for n in numeros:
                if numeros.count(n) == 1:
                    unicos.append(n)
            
            return unicos
        else:
            raise TypeError('El argumento ingresado no es válido. Por favor ingrese una lista o una tupla.')
    else:
        print('Ha ingresado un argumento vacío. Por favor utilice como argumento una lista o tupla con números.')


numeros = [1, 2, 1, 2, 3, 4, 5, 6, 6]

try:
    resultado = numeros_unicos(numeros)
    if resultado: 
        print('Lista de números:', numeros)
        print('Números únicos:', resultado)
except TypeError as e:
    print('ERROR:', e)

print()

numeros = []

try:
    resultado = numeros_unicos(numeros)
    if resultado: 
        print('Lista de números:', numeros)
        print('Números únicos:', resultado)
except TypeError as e:
    print('ERROR:', e)

print()

numeros = 'Hola'

try:
    resultado = numeros_unicos(numeros)
    if resultado: 
        print('Lista de números:', numeros)
        print('Números únicos:', resultado)
except TypeError as e:
    print('ERROR:', e)