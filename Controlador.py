import Modelo


def ListarProductos():
    con = Modelo.Conectar()
    listado = con.ListarProductos()
    print("\n| ID PRODUCTO   |   NOMBRE PRODUCTO    |   DESCRIPCIÓN   |   PRECIO   |  TIPO   |  INCLUYE PROMO   |   ID RECETA   |")
    for productos in listado:
        print(' ',productos[0],"\t\t",productos[1],"\t\t",str(productos[2])+"\t\t $"+str(producto[3]),"\t\t",producto[4],"\t\t",producto[5],"\t\t",producto[6])
    input("Para continuar presione enter")

def InsertarProductos():
    con = Modelo.Conectar()

    nombre = input("\nIngrese el nombre del Producto: ")
    decripción = input("\nIngrese el stock del Producto: ")
    precio = int(input("\nIngrese el precio del Producto: "))
    tipo = input("\nIngrese el tipo (Ejemplo Vegano, Vegetariano):")
    incluye_promo = input("\nIngrese si tiene promo (Ejemplo 3 x 2): ")

    #Aquí deberían brindarle la posibilidad al usuario de elegir una receta existente 
    # en la BD o que cree una receta nueva.

    nuevoProductos = Modelo.Productos(0,nombre,descripción,precio,tipo,incluye_promo,0)

    con.InsertarProductos(nuevoProductos)
    input("Para continuar presione enter")
