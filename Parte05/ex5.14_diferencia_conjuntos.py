# Ejercicio 5.14: Calcular la diferencia entre dos conjuntos.

escritorio = {'Notepad++', 'Atom', 'Eclipse', 'NetBeans', 'PyCharm'}
portatil = {'Notepad++', 'PyCharm', 'Visual Studio Code', 'IntelliJ IDEA'}

diferencia = escritorio.difference(portatil)
print(diferencia)

print('Los programas que hacen falta en el computador portatil son:', diferencia)

print()

diferencia = portatil.difference(escritorio)
print('Los programas que hacen falta en el computador de escritorio son:', diferencia)
