class Categoria:

    def __init__(self, codigo, nombre, descripcion):
        self.__Codigo = codigo
        self.__Nombre = nombre
        self.__Descripcion = descripcion
 
    def get_Codigo(self):
        return self.__Codigo
      
    def set_Codigo(self, codigo):
        self.__Codigo = codigo

    def get_Nombre(self):
        return self.__Nombre
      
    def set_Nombre(self, nombre):
        self.__Nombre = nombre

    def get_Descripcion(self):
        return self.__Descripcion
      
    def set_Descripcion(self, descripcion):
        self.__Descripcion = descripcion

    def __str__(self):
        return ('Categoría: ' + str(self.__Nombre) + '. Descripción: ' + str(self.__Descripcion))