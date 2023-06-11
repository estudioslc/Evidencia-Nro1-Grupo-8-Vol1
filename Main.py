
import Conexion as conexionBD
from Producto import Producto

print("Menu oprciones")
print("¿Quiere ingresar un producto?")
print("Para ingresar un producto ingrese Y")
print("Para ver el listado de los productos ingrese L")
ingresaProducto = int(input())
if ingresaProducto == Y:
    con = conexionBD.Conectar()
    nombreProducto = input("Ingrese el nombre del producto:")
    descripcionProducto = varchar(input("Ingrese caracteristicas principales del producto:"))
    precioProducto = decimal(input("Ingrese el precio del producto:"))
    tipoProducto = varchar(input("Ingrese si contiene tacc o no el producto:")
    incluyePromoProducto = vachar(input("Ingrese si el producto incluye promo:")

    producto = Producto(0,nombreProducto,descripcionProducto,precioProducto,tipoProducto,0)
    conexionBD.Insertar_Producto(producto)
    
elif  ingresaProducto == 2:
    con = conexionBD.Conectar()
    prod=conexionBD.Listado_De_Productos()
    for i in prod:
        print("Nombre:" + i[1] + "Stock:" + i[2] + "Precio" + i[3]+ "Unidad de medida del producto" + i[4])
