# Ejercicio 3. Comprobar el producto de mayor precio entre tres productos.

precio_1 = float(input('Escriba el precio del primer producto: '))

precio_2 = float(input('Escriba el precio del segundo producto: '))

precio_3 = float(input('Escriba el precio del tercer producto: '))

if precio_1 > precio_2 and precio_1 > precio_3:
    print('El primer producto es el de mayor precio ({})'.format(precio_1))
elif precio_2 > precio_3:
    print('El segundo producto es el de mayor precio ({})'.format(precio_2))
else: 
    print('El tercer producto es el de mayor precio ({})'.format(precio_3))


