import mysql.connector
class Conectar():

    def __init__(self) -> None:
        try:
            conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '*****',
                db='bd_Big_Bread'
            )
            if conexion.is_connected():
                print("LA CONEXION FUE EXITOSA")

        except:
            print("NO SE PUDO CONETAR A LA BASE DE DATOS")

        finally:
            if conexion.is_connected():
                conexion.close()
                print("LA CONEXION FUE CERRADA")
