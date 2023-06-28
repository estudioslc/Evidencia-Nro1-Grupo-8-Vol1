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

    def ActualizarProductos(self):
        if self.conexion.is_connected():
            try:
                select * from Productos;
                UPDATE Productos set Precio = 500 WHERE id_producto = 1;

    def EliminarProductos(self):
        if self.conexion.is_connected():
            try:
                DELETE from Productos WHERE Nombre LIKE 'Harina%';
                select * from Productos WHERE Nombre LIKE 'Harina%';

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
        self.ID_Receta = iD_Receta
    
    def getiD_producto(self):  #OBTENER EL VALOR DE ESTE EN ESPECIFICO: ID_PRODUCTO
        return self.iD_Producto
    def getnombre(self): #OBTENER EL VALOR DEL ATRIBUTO NOMBRE
        return self.nombre
    def getdescripción(self):
        return self.descripción
    def getprecio(self):
        return self.precio
    def gettipo(self):
        return self.tipo
    def getincluye_promo(self)
        return self.incluye_promo
    def getiD_Receta(self):
        return self.iD_Receta
    
    def setiD_producto(self,iD_Producto): #ASIGNO UN VALOR A ESTIBUTO. 
        self.iD_Producto = iD_Producto
    def setnombre(self,nombre): #ASIGNO UN VALOR A ESTIBUTO. nombrePRoducto=Tarta de coco.
        self.nombre = nombre
    def setdescripción(self,descripción):
        self.descripción = descripción
    def setprecio(self,precio):
        self.precio = precio
    def settipo(self,tipo):
        self.tipo = tipo
    def setincluye_promo(self)
        self.incluye_promo = incluye_promo
    def setiD_Receta(self,iD_Receta):
        self.iD_Receta = iD_Receta   

class Pedido():
    id_producto = 0,
    id_producción = "",
    Fecha = 0,
    Cantidad = 0,
    Cliente = 0,
    Tipo_de_entrega = "",

    def __init__(self,iD_Producto,iD_Producción,fecha,cantidad,cliente,tipo_de_entrega):
        self.id_producto = iD_Producto
        self.id_producción = iD_Producción
        self.Fecha = fecha
        self.Cantidad = cantidad
        self.Cliente = cliente
        self.Tipo_de_entrega = tipo_de_entrega
    
    def getiD_producto(self):  #OBTENER EL VALOR DE ESTE EN ESPECIFICO: ID_PRODUCTO
        return self.iD_Producto
    def getiD_producción(self): #OBTENER EL VALOR DEL ATRIBUTO NÚMERO DE PRODUCCIÓN
        return self.iD_Producción
    def getfecha(self):
        return self.fecha
    def getcantidad(self):
        return self.cantidad
    def getcliente(self):
        return self.cliente
    def gettipo_de_entrega(self)
        return self.tipo_de_entrega
        
    def setiD_Producto(self,iD_Producto): #ASIGNO UN VALOR A ESTIBUTO. 
        self.iD_Producto = iD_Producto
    def setiD_Producción(self,iD_Producción):
        self.iD_Producción = iD_Producción
    def setfecha(self,fecha):
        self.fecha = fecha
    def setcantidad(self,cantidad):
        self.cantidad = cantidad
    def setcliente(self,cliente):
        self.cliente = cliente
    def settipo_de_entrega(self,tipo_de_entrega)
        self.tipo_de_entrega = tipo_de_entrega

class Insumos():
    id_ingrediente = 0,
    Nombre = "",
    Descripción = 0,
    Contiene alérgeno = 0,
    Cantidad = 0,
    
    def __init__(self,iD_Ingrediente,nombre,descripción,contiene_alérgeno,cantidad):
        self.id_ingrediente = iD_Ingrediente
        self.Nombre = nombre
        self.Descripción = descripción
        self.Contiene_alérgeno = contiene_alérgeno
        self.Cantidad = cantidad

    def getiD_Ingredientes(self):
        return self.iD_Ingredientes
    def getnombre(self):
        return self.nombre
    def getdescripción(self):
        return self.descripción
    def getcontiene_alérgeno(self):
        return self.contiene_alérgeno
    def getcantidad(self):
        return self.cantidad
        
    def setiD_Ingredientes(self,iD_Ingredientes): 
        self.iD_Ingredientes = iD_Ingredientes
    def setnombre(self,nombre):
        self.nombre = nombre
    def setdescripción(self,descripción):
        self.descripción = descripción
    def setcontiene_alérgeno(self,contiene_alérgeno):
        self.contiene_alérgeno = contiene_alérgeno
    def setcantidad(self,cantidad):
        self.cantidad = cantidad
