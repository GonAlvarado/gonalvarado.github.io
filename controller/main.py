import sys
sys.path.append('C:\proyectoIntegrador1\model')
#from logging import exception
from pedido import *
from producto import *
from CRUDProductos import *

pedido = Pedido()
dao = DAOProductos()

def menu():
    try:
        continuar = True
        while(continuar):
            opcion_valida = False
            while(not opcion_valida):
                print('***************** MENU PRINCIPAL *****************')
                print('1 - Listar productos')
                print('2 - Cargar producto')
                print('3 - Eliminar producto')
                print('4 - Buscar producto')
                print('5 - Actualizar precio producto')
                print('6 - Añadir producto al carrito')
                print('7 - Quitar producto del carrito')
                print('8 - Finalizar compra')
                print('9 - Salir')
                print('*' * 50)
                opcion = int(input('Seleccione una opción: '))
                if opcion < 1 or opcion > 9:
                    print('Opción incorrecta, ingrese nuevamente...')
                elif opcion == 9:
                    continuar = False
                    print('¡Gracias por utilizar el sistema!')
                    break
                else:
                    opcion_valida = True
                    ejecutar_opcion(opcion)
    except Exception as e:
        print(e)

def ejecutar_opcion(opcion):
    try:
        if opcion == 1:
            dao.listar_productos()
        elif opcion == 2:
            nombre = input('Ingrese nombre del producto: ')
            marca = input('Ingrese marca del producto: ')
            precio = int(input('Ingrese precio del producto: '))
            descripcion = input('Ingrese descripción del producto: ')
            imagen = input('Ingrese imagen del producto: ')
            dao.listar_categorias()
            categoria = int(input('Ingrese código de categoria del producto: '))
            dao.insertar_producto(nombre, marca, precio, descripcion, imagen, categoria)
        elif opcion == 3:
            dao.listar_productos()
            codigo = input('Ingrese código de producto a eliminar: ')
            dao.eliminar_producto(codigo)
        elif opcion == 4:
            nombre = input('Ingrese nombre del producto: ')
            dao.buscar_producto(nombre)
        elif opcion == 5:
            dao.listar_productos()
            codigo = input('Ingrese codigo de producto: ')
            precio = int(input('Ingrese nuevo precio: '))
            dao.actualizar_producto(codigo, precio)
        elif opcion == 6:
            dao.listar_productos()
            nom = input('Ingrese el nombre del producto que desee agregar: ')
            data = dao.buscar_producto(nom)
            producto = Producto(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6])
            cantidad = int(input('Ingrese la cantidad que desea agregar: '))
            pedido.agregar_producto(producto, cantidad)
        elif opcion == 7:
            pedido.mostrar_productos()
            codigo = int(input('Ingrese el codigo del producto que desee quitar: '))
            cantidad = int(input('Ingrese la cantidad que desea quitar: '))
            for i in pedido.productos:
                if i.Codigo == codigo:
                    pedido.quitar_producto(i, cantidad)
        elif opcion == 8:
            pedido.mostrar_productos()
            print ('El total del pedido es: ' + str(pedido.total_pedido()))
    except Exception as e:
        print(e)

menu()