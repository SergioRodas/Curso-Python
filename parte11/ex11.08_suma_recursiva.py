# Ejercicio 11.8: Crear una función recursiva para sumar los números de una lista.

def sumar_recursivamente(numeros):
    """
    Suma los elementos de una lista
    
    Parameters:
    numeros: Lista de valores numéricos

    Returns:
    Suma de los valores de la lista.
    """
    if len(numeros) == 0:
        return 0
    else:
        return numeros[0] + sumar_recursivamente(numeros[1:])
 
valores = [1, 2, 3, 4, 5]

try:
    resultado = sumar_recursivamente(valores)

    print('La suma es igual a:', resultado)
except TypeError as e:
    print('ERROR:', e)