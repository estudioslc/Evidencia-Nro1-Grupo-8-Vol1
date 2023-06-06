import mysql.connector

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
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó la base de datos!',descripcionError")
            
        finally:
            if self.conexion.is_connected():
                self.conexion.close()
                print("LA CONEXION FUE CERRADA")
            
