class Venta:

    def __init__(self, codigo, fecha, pedido, factura):
        self.__Codigo = codigo
        self.__Fecha = fecha
        self.__Pedido = pedido
        self.__Factura = factura
 
    def get_Codigo(self):
        return self.__Codigo
      
    def set_Codigo(self, codigo):
        self.__Codigo = codigo

    def get_Fecha(self):
        return self.__Fecha
      
    def set_Fecha(self, fecha):
        self.__Fecha = fecha

    def get_Pedido(self):
        return self.__Pedido
      
    def set_Pedido(self, pedido):
        self.__Pedido = pedido

    def get_Factura(self):
        return self.__Factura
      
    def set_Factura(self, factura):
        self.__Factura = factura

    def __str__(self):
        return ('Código de venta: ' + str(self.__Codigo) + '. \nFecha: ' + str(self.__Fecha) + '. \nPedido: ' + str(self.__Pedido) + '. \nFactura: ' + str(self.__Factura))
    