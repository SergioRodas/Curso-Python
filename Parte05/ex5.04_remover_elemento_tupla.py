# Ejercicio 5.4: Remover un elemento (valor) de una tupla.

meses_del_anio = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

print('Contenido de la tupla:', meses_del_anio)
print('Cantidad de elementos de la tupla:', len(meses_del_anio))

print()

meses_del_anio = list(meses_del_anio)
meses_del_anio.remove('Enero')
meses_del_anio = tuple(meses_del_anio)

print('Contenido de la tupla:', meses_del_anio)
print('Cantidad de elementos de la tupla:', len(meses_del_anio))