class Factura:

    def __init__(self, numero, tipo, fecha, detalle, total):
        self.__Numero = numero
        self.__Tipo = tipo
        self.__Fecha = fecha
        self.__Detalle = detalle
        self.__Total = total
 
    def get_Numero(self):
        return self.__Numero
      
    def set_Numero(self, numero):
        self.__Numero = numero

    def get_Tipo(self):
        return self.__Tipo
      
    def set_Tipo(self, tipo):
        self.__Tipo = tipo

    def get_Fecha(self):
        return self.__Fecha
      
    def set_Fecha(self, fecha):
        self.__Fecha = fecha

    def get_Detalle(self):
        return self.__Detalle
      
    def set_Detalle(self, detalle):
        self.__Detalle = detalle

    def get_Total(self):
        return self.__Total
      
    def set_Total(self, total):
        self.__Total = total

    def __str__(self):
        return ('Factura: ' + str(self.__Numero) + '. \nTipo: ' + str(self.__Tipo) + '. \nFecha: ' + str(self.__Fecha) + '. \nDetalle: ' + str(self.__Detalle) + '. \nTotal: $' + str(self.__Total))