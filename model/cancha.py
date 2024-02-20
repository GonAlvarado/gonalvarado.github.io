class Cancha:

    def __init__(self, codigo, descripcion, disciplina, precio):
        self.__Codigo = codigo
        self.__Descripcion = descripcion
        self.__Disciplina = disciplina
        self.__Precio = precio
 
    def get_Codigo(self):
        return self.__Codigo
      
    def set_Codigo(self, codigo):
        self.__Codigo = codigo

    def get_Descripcion(self):
        return self.__Descripcion
      
    def set_Descripcion(self, descripcion):
        self.__Descripcion = descripcion

    def get_Disciplina(self):
        return self.__Disciplina
      
    def set_Disciplina(self, disciplina):
        self.__Disciplina = disciplina

    def get_Precio(self):
        return self.__Precio
      
    def set_Precio(self, precio):
        self.__Precio = precio

    def __str__(self):
        return (str(self.__Descripcion) + '. Disciplina: '+ str(self.__Disciplina) + '. Precio: ' + str(self.__Precio))