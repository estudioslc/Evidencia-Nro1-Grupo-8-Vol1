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
            
            
            
