# Ejercicio 9.7: Construir un patrón con asteriscos que represente la letra E.

# *****
# *
# *
# ****
# *
# *
# *****

for i in range(7):
    if i == 0 or i == 6:
        print('*****')
    elif i == 3:
        print('****')
    else:
        print('*')