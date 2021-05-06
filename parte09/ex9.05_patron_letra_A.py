# Ejercicio 9.5: Construir un patrón con asteriscos que represente la letra A.

#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

for i in range(7):
    if i == 0:
        print(' ***')
    elif i == 3:
        print('*****')
    else:
        print('*   *')