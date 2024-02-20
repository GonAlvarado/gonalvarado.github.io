class Producto: 
    Codigo = 0
    Nombre = ""
    Marca = ""
    Precio = 0
    Descripcion = ""
    Imagen = ""

    def __init__(self, codigo, nombre, marca, precio, descripcion, imagen, categoria):
        self.Codigo = codigo
        self.Nombre = nombre
        self.Marca = marca
        self.Precio = precio
        self.Descripcion = descripcion
        self.Imagen = imagen
        self.Categoria = categoria

    def get_Codigo(self):
        return self.Codigo

    def set_Codigo(self, codigo):
        self.Codigo = codigo 
    
    def get_Nombre(self):
        return self.Nombre

    def set_Nombre(self, nombre):
        self.Nombre = nombre

    def get_Marca(self):
        return self.Marca

    def set_Marca(self, marca):
        self.Marca = marca

    def get_Precio(self):
        return self.Precio

    def set_Precio(self, precio):
        self.Precio = precio

    def get_Descripcion(self):
        return self.Descripcion

    def set_Descripcion(self, descripcion):
        self.Descripcion = descripcion

    def get_Imagen(self):
        return self.Imagen

    def set_Imagen(self, imagen):
        self.Imagen = imagen

    def get_Categoria(self):
        return self.Categoria

    def set_Categoria(self, categoria):
        self.Categoria = categoria

    def __str__(self):
        return ('El código del producto es:' + str(self.Codigo) + ' su nombre es:' + str(self.Nombre) + ' El precio del producto es: '+ str(self.Precio) )

    def calcular_total(self, unidades):
        return (self.Precio * unidades)
