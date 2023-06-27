import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '****',
                db = 'BigBread'

            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)
    
    def ListarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT * FROM Productos"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)
    
    def InsertarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into productos values(null,%s,%s,%s,%s,null)"

                data = (productos.getNombre(),
                        productos.getDescripción(),
                        productos.getPrecio(),
                        productos.getTipo(),
                        productos.getIncluye_promo()
                        )

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Producto insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

class Productos():
    ID_Producto = 0,
    Nombre = "",
    Descripción = 0,
    Precio = 0,
    Tipo = 0,
    Incluye_promo = "",
    ID_Receta = 0

    def __init__(self,iD_Producto,nombre,descripción,precio,tipo,incluye_promo,iD_Receta):
        self.ID_Producto = iD_Producto
        self.Nombre = Nombre
        self.Descripción = stock
        self.Precio = precio
        self.Tipo = tipo
        self.Incluye_promo = incluye_promo
        self.ID_Receta =iD_Receta
    
    def getiD_Producto(self):  #OBTENER EL VALOR DE ESTE EN ESPECIFICO: ID_PRODUCTO
        return self.iD_Producto
    def getnombre_Producto(self): #OBTENER EL VALOR DEL ATRIBUTO NOMBRE_PRODUCTO
        return self.nombre_Producto
    def getstock(self):
        return self.stock
    def getprecio(self):
        return self.precio
    def getunidad_de_medida(self):
        return self.unidad_de_medida
    def getiD_Receta(self):
        return self.iD_Receta
    
    def setiD_Producto(self,iD_Producto): #ASIGNO UN VALOR A ESTIBUTO. 
        self.iD_Producto = iD_Producto
    def setnombre_Producto(self,nombre_Producto): #ASIGNO UN VALOR A ESTIBUTO. nombrePRoducto=Harina de arroz.
        self.nombre_Producto = nombre_Producto
    def setstock(self,stock):
        self.stock = stock
    def setprecio(self,precio):
        self.precio = precio
    def setgetunidad_de_medida(self,getunidad_de_medida):
        self.getunidad_de_medida = getunidad_de_medida
    def setiD_Receta(self,iD_Receta):
        self.iD_Receta = iD_Receta   
