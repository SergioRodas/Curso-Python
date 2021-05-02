# Ejercicio 3. Calcular área de un trapezoide.

base_inferior = float(input('Ingrese la base inferior(B): '))
base_superior = float(input('Ingrese la base superior(b): '))
altura = float(input('Ingrese la altura (h): ')) 

area = (base_inferior + base_superior)/ 2 * altura 
print('El área del trapezoide es igual a:', area)