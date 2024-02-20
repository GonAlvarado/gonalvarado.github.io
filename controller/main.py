import sys
sys.path.append('C:\proyectoIntegrador1\model')
from logging import exception
from pedido import *
from producto import *

# Productos de Prueba

producto1 = Producto(1, "Adipower", "Adidas", 5000, "Paleta Adidas para niños", "paleta1.jpg", "Paletas")
producto2 = Producto(2, "Vertex", "Bullpadel", 15000, "Paleta Bullpadel para jugadores avanzados", "paleta2.jpg", "Paletas")
producto3 = Producto(3, "Control", "Adidas", 2000, "Bolso paletero tipo mochila", "accesorio1.jpg", "Accesorios")

pedido = Pedido()

try:
    pedido.agregar_producto(producto1,15)
    pedido.agregar_producto(producto2,15)
    pedido.agregar_producto(producto3,8)

    print ('El total del pedido es: ' + str(pedido.total_pedido()))

    pedido.mostrar_productos()

    pedido.quitar_producto(producto2, 13)

    pedido.mostrar_productos()

except Exception as e:
    print(e)