# Ejercicio 5.7: Seleccionar de forma aleatoria un elemento de una lista.
import random

# Solución 1:
print('Solución 1:')

print()

meses_del_anio = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
numero_aleatorio = random.randint(0, len(meses_del_anio)-1)
mes_aleatorio = meses_del_anio[numero_aleatorio]
print('El mes aleatorio elegido es:', mes_aleatorio)

print()

# Solución 2:
print('Solución 2:')

print()

mes_aleatorio = random.choice(meses_del_anio)
print('El mes aleatorio elegido es:', mes_aleatorio)