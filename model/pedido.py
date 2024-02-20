from producto import *

class Pedido:

    productos = []
    cantidades = []

    def __init__(self):
        self.productos = []
        self.cantidades = []

    def agregar_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception('Error al agregar producto: producto debe ser de la clase Producto')
        
        if not isinstance(cantidad, int):
            raise Exception('Error al agregar producto: cantidad debe ser un número')

        if cantidad <=0 :
            raise Exception('Error al agregar producto: cantidad debe ser número mayor a cero')

        if producto in self.productos : 
            indice = self.productos.index(producto)
            self.cantidades[indice] += cantidad
        else: 
            self.cantidades.append(cantidad)
            self.productos.append(producto)
    
    def quitar_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception('Error al quitar producto: producto debe ser de la clase Producto')
        
        if not isinstance(cantidad, int):
            raise Exception('Error al quitar producto: cantidad debe ser un número')

        if cantidad <=0 :
            raise Exception('Error al quitar producto: cantidad debe ser número mayor a cero')
        
        if producto in self.productos : 
            indice = self.productos.index(producto)
            self.cantidades[indice] -= cantidad
            if self.cantidades[indice] <=0 :
                indice = self.productos.index(producto)
                del self.productos[indice]
                del self.cantidades[indice] 
        else: 
            raise Exception('Error al quitar producto: El producto no existe')
    
    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.productos,self.cantidades):
            total += p.calcular_total(c)
        
        return total 
    
    def mostrar_productos(self): 
        for (p,c) in zip(self.productos,self.cantidades):
            print('Producto:' + p.get_Nombre() + ', Cantidad:' + str(c))