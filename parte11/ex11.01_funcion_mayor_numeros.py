# Ejercicio 11.1: Crear una función para obtener el mayor de 3 números.

# a, b, c

def mayor_de_tres(a, b, c):
    if a == b and b == c:
        return None  
    elif a > b and a > c:
        return a
    elif b > c:
        return b
    else: 
        return c
        
    


a = 18
b = 17
c = 18
mayor = mayor_de_tres(a, b, c)

if mayor:
    print(f'El mayor entre {a}, {b} y {c} es {mayor}.')
else:
    print('Los tres números son iguales. Ninguno es mayor.')

