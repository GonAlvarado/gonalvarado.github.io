import mysql.connector

class DAOProductos:

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'cuartoset'
            )
        except mysql.connector.Error as descripcionError:
            print("La conexión falló. Descripción:", descripcionError)

    def insertar_producto(self, nombre, marca, precio, descripcion, imagen, categoria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "INSERT INTO `productos` (`codigo_prod`, `nombre_prod`, `marca_prod`, `precio_prod`, `descripcion_prod`, `imagen_prod`, `cod_cat_prod`) VALUES (NULL, %s, %s, %s, %s, %s, %s);"
                data = (nombre, marca, precio, descripcion, imagen, categoria)
                cursor.execute(query, data)
                self.conexion.commit()
                self.conexion.close()
                print("Se insertó el producto exitosamente.")
            except:
                print("La inserción falló.")
   
    def buscar_producto(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query= "SELECT * FROM `productos` WHERE `nombre_prod` LIKE '%{}%'".format(nombre)
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                self.conexion.close()
            except:
                print("No se encontraron productos.")

    def eliminar_producto(self, codigo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM productos WHERE `productos`.`codigo_prod` = {}".format(codigo)
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
                self.conexion.close()
            except:
                print("La eliminación falló.")

    def actualizar_producto(self, codigo, precio):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE `productos` SET `precio_prod` = '{}' WHERE `productos`.`codigo_prod` = {}".format(precio, codigo)
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
                self.conexion.close()
            except:
                print("La actualización falló.")

    def listar_productos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query= "SELECT * FROM `productos`"
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                self.conexion.close()
            except:
                print("No se encontraron productos.")