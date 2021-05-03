# Ejercicio 9.1: Construir un patrón con el carácter asterisco.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * 
# * * * 
# * *
# *

asterisco = '* '
patron = ''

for i in range(5):
    patron += asterisco
    print(patron)

for i in range(4):
    patron = patron[:-2]
    print(patron)
   