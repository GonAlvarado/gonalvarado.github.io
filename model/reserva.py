class Reserva:

    def __init__(self, numero, fecha, hora, usuario, cancha):
        self.__Numero = numero
        self.__Fecha = fecha
        self.__Hora = hora
        self.__Usuario = usuario
        self.__Cancha = cancha
 
    def get_Numero(self):
        return self.__Numero
      
    def set_Numero(self, numero):
        self.__Numero = numero

    def get_Fecha(self):
        return self.__Fecha
      
    def set_Fecha(self, fecha):
        self.__Fecha = fecha
        
    def get_Hora(self):
        return self.__Hora
      
    def set_Hora(self, hora):
        self.__Hora = hora

    def get_Usuario(self):
        return self.__Usuario
      
    def set_usuario(self, usuario):
        self.__Usuario = usuario

    def get_Cancha(self):
        return self.__Cancha
      
    def set_Cancha(self, cancha):
        self.__Cancha = cancha

    def __str__(self):
        return ('Reserva: ' + str(self.__Numero) + '. \nFecha: ' + str(self.__Fecha) + '. \nHora: ' + str(self.__Hora) + '. \nCancha: ' + str(self.__Cancha) + '. \nUsuario: ' + str(self.__Usuario))