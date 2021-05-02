# Ejercicio 7. Categorizar según la cantidad de puntos obtenidos por un jugador.

# +----------+---------------+
# | Puntos   | Categoría     |
# +----------+---------------+
# | 0-100    | Principiante  |
# +----------+---------------+
# | 101-500  | Estándar      |
# +----------+---------------+
# | 501-2000 | Experimentado |
# +----------+---------------+
# | 2000>    | Máster        |
# +----------+---------------+
 
puntos = int(input('Digite la cantidad de puntos obtenidos: '))

if 0 <= puntos <= 100:
    print('Usted está en la categoría `principiante`.')
elif 101 <= puntos <= 500:
    print('Usted está en la categoría `estándar`.')
elif 501 <= puntos <= 2000:
    print('Usted está en la categoría `experimentado`.')
elif puntos >= 2000:
    print('Usted está en la categoría `máster`.')

else:
    print('La cantidad ingresada no es valida.')