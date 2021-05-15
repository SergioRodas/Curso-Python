# Programa Python:

def saludar(mensaje):
    print(mensaje)

class Persona:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre

sergio = Persona(123456789, 'Sergio Rodas')

saludo = f'Hola, mi nombre es {sergio.nombre}.'

saludar(saludo)