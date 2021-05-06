# Ejercicio 9.9: Construir un patrón con asteriscos que represente la letra Z.

# *******
#      *
#     *
#    *
#   * 
#  *
# *******

for i in range(7):
    if i == 0 or i == 6:
        print('*' * 7)
    else:
        print(' ' * (6 - i) + '*')