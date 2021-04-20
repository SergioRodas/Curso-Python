# Ejercicio 5.15: Calcular la diferencia simétrica entre dos conjuntos.

escritorio = {'Notepad++', 'Atom', 'Eclipse', 'NetBeans', 'PyCharm'}
portatil = {'Notepad++', 'PyCharm', 'Visual Studio Code', 'IntelliJ IDEA'}

diferencia_simetrica = escritorio.symmetric_difference(portatil)
print('Contenido del conjunto `diferencia_simetrica`:', diferencia_simetrica)