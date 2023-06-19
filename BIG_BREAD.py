import mysql.connector

from Producto import Producto
class Conectar_Base_de_Datos():
    
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '*****',
                db = 'bd_BIG_BREAD'
            )
            if self.conexion.is_connected():
                print("LA CONEXION FUE EXITOSA")
                
        except:
            print("¡No se conectó la base de datos!',descripcionError")
            
            
    def Insertar_Productos(self,producto):
        if self.conexion.is_connected():
         try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "INSERT INTO productos values(%s,%s,%s,%s,%s,%s)"
            data = (producto.getid_productos(),
                    producto.getnombre(),
                    producto.getdescripcion(),
                    producto.getPrecio(),
                    producto.getTipo(),
                    producto.getIncluye_promo()
                    )
            
            cursor.execute(sentenciaSQL,data)
            cursor.Conexion.commit()
            cursor.Conexion.close()   
            print("Producto insertado correctamente")

          except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)
            
def Listado_De_Productos(self):
    if self.conexion.is_connected():
        try:
            cursor = self.conexion.cursor()
            sentenciaSQL = "SELECT * FROM Productos"
            cursor.execute(sentenciaSQL)
            resultados= cursor.fetchall()
            cursor.Conexion.close()
            return resultados
            
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conctar la Base de Datos", descripcionDelError)
            
UPDATE Productos set Precio = 500 WHERE Id_Producto = 1;

DELETE from Productos WHERE Incluye_promo LIKE 'SI%';
select * from Productos WHERE Incluye_promo LIKE 'SI%';
