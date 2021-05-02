# Ejercicio 2. Convertir radianes a grados.
from math import pi

radianes = float(input('Digite los radianes: '))

grados = 180 * radianes / pi

print('{} radianes son equivalentes a {} grados'.format(radianes, grados))