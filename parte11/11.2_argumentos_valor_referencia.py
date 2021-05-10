# Pasar argumentos por valor y por referencia: 
print('Pasar argumentos por valor y por referencia: ')

# 1. Pasar argumentos por valor:
print('1. Pasar argumentos por valor:')

def duplicar(numero):
    numero *= 2
    print('El número duplicado es igual a:', numero)

x = 2
print('El valor de la variable `x` antes de su duplicación:', x)

duplicar(x)

print('El valor de la variable `x` después de su duplicación:', x)

print()

# 2. Pasar argumentos por referencia:
print('2. Pasar argumentos por referencia:')

def agregar_elementos(lista):
    lista.append(2)

numeros = [1]
print('Contenido de la variable `numeros` antes de invocar `agregar_elementos`:', numeros)

agregar_elementos(numeros)

print('Contenido de la variable `numeros` después de invocar `agregar_elementos`:', numeros)