from .inventario_funciones import registrar_producto, realizar_venta, buscar_producto, ventas_rango_fecha, top_5_mas_vendidos, top_5_menos_vendidos

def mostrar_menu():
    """
    Muestra el menú de las operaciones disponibles.
    """
    print('1. Registrar nuevo producto.')
    print('2. Vender un producto.')
    print('3. Buscar un producto por su código.')
    print('4. Cambiar disponibilidad de un producto.')
    print('5. Productos vendidos en un rango de fecha.')
    print('6. Ver top 5 de los productos más vendidos.')
    print('7. Ver top 5 de los productos menos vendidos.')
    print('0. Salir.')

def capturar_entero(mensaje):
    """
    Captura un número entero. Valida el ingreso de datos.

    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de un número.

    Returns:
    Número entero resultado de la captura.
    """
    while True:
        try:
            numero = int(input(f'{mensaje}: '))

            return numero
        except ValueError:
            print('ERROR: Debe digitar un número entero.')
        
        print()

def capturar_real(mensaje):
    """
    Captura un número real. Valida el ingreso de datos.

    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de un número.

    Returns:
    Número real resultado de la captura.
    """
    while True:
        try:
            numero = float(input(f'{mensaje}: '))

            return numero
        except ValueError:
            print('ERROR: Debe digitar un número real.')
        
        print()

def capturar_cadena(mensaje):
    """
    Captura una cadena de caracteres. Valida el ingreso de datos.

    Parameters:
    mensaje: Mensaje o texto personalizado a mostrar para la captura de una cadena de caracteres.

    Returns:
    Cadena de caracteres.
    """
    while True:
        cadena = input(f'{mensaje}: ').strip()

        if len(cadena):
            return cadena
        else:
            print('MENSAJE: Debe digitar una cadena de caracteres con texto.')
        
        print()

def main():
    productos = []
    while True:
        while True:
            mostrar_menu()
            try:
                opcion = int(input('Digite la opción: '))
                if 0 <= opcion >= 7:
                    break
                else:
                    print('MENSAJE: Debe digitar un número que esté dentro del rango de opciones.')
            except ValueError:
                print('ERROR: Debe digitar un número entero válido.')
        
        if opcion == 0:
            break
        elif opcion == 1:


    print()
    print('El programa ha finalizado.')

if __name__ = '__main__':
    main()