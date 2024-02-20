class Usuario:

    def __init__(self, dni, nombre, apellido, correo, domicilio, usuario, contrasenia):
        self.Dni = dni
        self.Nombre = nombre
        self.Apellido = apellido
        self.Correo = correo
        self.Domicilio = domicilio
        self.Usuario = usuario
        self.Contrasenia = contrasenia
 
    def get_Dni(self):
        return self._Dni
      
    def set_Dni(self, dni):
        self._Dni = dni

    def get_Nombre(self):
        return self._Nombre
      
    def set_Nombre(self, nombre):
        self._Nombre = nombre

    def get_Apellido(self):
        return self._Apellido
      
    def set_Apellido(self, apellido):
        self._Apellido = apellido

    def get_Correo(self):
        return self._Correo
      
    def set_Correo(self, correo):
        self._Correo = correo

    def get_Domicilio(self):
        return self._Domicilio
      
    def set_Domicilio(self, domicilio):
        self._Domicilio = domicilio

    def get_Usuario(self):
        return self._Usuario
      
    def set_Usuario(self, usuario):
        self._Usuario = usuario

    def get_Contrasenia(self):
        return self._Contrasenia
      
    def set_Contrasenia(self, contrasenia):
        self._Contrasenia = contrasenia

    def __str__(self):
        return ('El usuario ' + str(self.Usuario) + ' corresponde a ' + str(self.Nombre) + ' '+ str(self.Apellido) + ', DNI número ' + str(self.Dni))