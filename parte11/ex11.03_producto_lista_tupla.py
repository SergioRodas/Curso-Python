# Ejercicio 11.3: Crear una función para multiplicar todos los números en una lista o tupla.

def multiplicar(valores):
    """
    Multiplica el conjunto o grupo de valores de una lista o tupla.

    Parameters:
    valores: Lista o tupla con los valores a multiplicar.

    Returns:
    Producto de los valores en la lista o tupla.
    """
    if isinstance(valores, (list, tuple)):
        if len(valores):
            producto = 1
            for v in valores:
                producto *= v
            
            return producto
        else:
            return None
    else:
        raise ValueError('Ha pasado un argumento que no es una lista ni una tupla.')

try:
    numeros = [1, 2, 3, 4, 5]
    resultado = multiplicar(numeros)
    print('El resultado de multiplicar los numeros {} es igual a {}'.format(numeros, resultado))
except ValueError as e:
    print('ERROR:', e)

print()

precios = (999.9, 59.9, 27.5)

try:
    resultado = multiplicar(precios)
    print('El resultado de multiplicar los precios {} es igual a {}'.format(precios, resultado))
except ValueError as e:
    print('ERROR:', e)

print()

numeros = 1000

try:
    resultado = multiplicar(numeros)
    print('El resultado de multiplicar los numeros {} es igual a {}'.format(numeros, resultado))
except ValueError as e:
    print('ERROR:', e)

print()

numeros = []

try:
    resultado = multiplicar(numeros)
    if resultado:
        print('El resultado de multiplicar los numeros {} es igual a {}'.format(numeros, resultado))
    else:
        print('No ha proveído datos para la lista o tupla. Está vacía.')
except ValueError as e:
    print('ERROR:', e)