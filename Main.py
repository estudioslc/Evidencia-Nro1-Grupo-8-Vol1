import Controlador

while True:
    print("\n+-------------------------------------------------------+")
    print("|    BIENVENIDO AL SISTEMA INFORMÁTICO DE BIG BREAD SA    |")
    print("+-------------------------------------------------------+\n")
    print("")
  
    print("MENÚ PRINCIPAL\n")
    print("1 - INGRESAR / ELIMINAR / MODIFICACION DE PRODUCTO")
    print("2 - LISTADO DE PRODUCTOS")
    print("0 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        Controlador.InsertarProducto()
    elif opcion == 2:
        Controlador.ListarProductos()
    elif opcion == 0:
        break
    else:
        print("¡ERROR - Opción incorrecta!")
