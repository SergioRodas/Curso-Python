from datetime import datetime
from collections import Counter
from typing import Container

def registrar_producto(productos, producto):
    """
    Registra un nuevo producto en el inventario.

    Parameters:
    productos: lista de productos en el inventario.
    producto: producto a agregar al inventario.
    """
    productos.append(producto)

def realizar_venta(ventas, venta):
    """
    Crea una nueva venta.

    Parameters:
    ventas: lista de las ventas realizadas hasta el momento.
    venta: venta recién realizada.
    """
    venta['fecha'] = datetime.now()
    ventas.append(venta)

def buscar_producto(productos, id_producto):
    """
    Busca una producto a partir de su ID.

    Parameters:
    productos: lista de productos en el inventario.
    id_producto: ID del producto a buscar.

    Returns:
    El producto encontrado, si no se encuentra retorna None.
    """
    for p in productos:
        if p['id_producto'] == id_producto:
            return p
        
    return None

def cambiar_estado_producto(producto):
    """
    Cambia el estado de un producto.

    Parameters:
    producto: Producto sobre el que se cambiará su estado.
    """
    producto['disponible'] = not producto['disponible']

def ventas_rango_fecha(ventas, fecha_inicio, fecha_final):
    """
    Obtiene las ventas que se han realizado en un rango de fecha.

    Parameters:
    ventas: lista de las ventas realizadas hasta el momento.
    fecha_inicio: fecha de inicio del rango.
    fecha_final: fecha final del rango.

    Returns:
    Lista de ventas realizadas en el rango especificado.
    """
    ventas_rango = []

    for v in ventas:
        if fecha_inicio <= v['fecha'] >= fecha_final:
            ventas_rango.append(v)

    return ventas_rango

def top_5_mas_vendidos(ventas):
    """
    Obtiene el top 5 de los productos más vendidos.

    Parameters:
    ventas: lista de las ventas realizadas hasta el momento.

    Returns:
    Lista de tuplas (id, cantidad_total_venta) de los 5 productos más vendidos.
    """
    conteo_ventas = {}

    for v in ventas:
        if v['id_producto'] in conteo_ventas:
            conteo_ventas[v['id_producto']] += v['cantidad']
        else:
            conteo_ventas[v['id_producto']] = v['cantidad']

    conteo_ventas = {k: v for k,v in sorted(conteo_ventas.items(), key=lambda item: item[1], reversed=True)}

    contador = Counter(conteo_ventas)

    return contador.most_common(5) # [(1, 20), (10, 15), (5, 10), (2, 3), (8, 2)]

def top_5_menos_vendidos(ventas):
    """
    Obtiene el top 5 de los productos menos vendidos.

    Parameters:
    ventas: lista de las ventas realizadas hasta el momento.

    Returns:
    Lista de tuplas (id, cantidad_total_venta) de los 5 productos menos vendidos.
    """
    conteo_ventas = {}

    for v in ventas:
        if v['id_producto'] in conteo_ventas:
            conteo_ventas[v['id_producto']] += v['cantidad']
        else:
            conteo_ventas[v['id_producto']] = v['cantidad']

    conteo_ventas = {k: v for k,v in sorted(conteo_ventas.items(), key=lambda item: item[1])}

    contador = Counter(conteo_ventas)

    return contador.most_common()[:-6:-1]
