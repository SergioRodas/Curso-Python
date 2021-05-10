# Parametros/argumentos nombrados variables - keywords:
print('Parametros/argumentos nombrados variables - keywords:')

def mostrar_identidad(**identificacion):
    resultado = ''  

    if identificacion.get('documento'):
        resultado += 'Documento: ' + identificacion.get('documento') + '\n'
    if identificacion.get('nombre'):
        resultado += 'Nombre: ' + identificacion.get('nombre') + '\n'
    if identificacion.get('apellido'):
        resultado += 'Apellido: ' + identificacion.get('apellido') + '\n'
    
    return resultado

persona = mostrar_identidad(nombre='Sergio', apellido='Rodas')
print('Identificación: \n', persona)

print()

persona = mostrar_identidad(nombre='Sergio', apellido='Rodas', documento='40734163')
print('Identificación:\n', persona)

