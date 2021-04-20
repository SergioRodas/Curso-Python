# Ejercicio 5.2: Invertir el contenido de una tupla.

meses_del_anio = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
print(type(meses_del_anio))
print(meses_del_anio)

print()

# SOLUCIÓN 1:
print('Solución 1:')

meses_del_anio_inversos = []

for i in range(len(meses_del_anio) -1, -1, -1):
    meses_del_anio_inversos.append(meses_del_anio[i])

meses_del_anio_inversos = tuple(meses_del_anio_inversos)
print(type(meses_del_anio_inversos))
print(meses_del_anio_inversos)

print()

# SOLUCIÓN 2:
print('Solución 2:')
meses_invertidos = tuple(reversed(meses_del_anio))
print(meses_invertidos)