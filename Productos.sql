CREATE DATABASE BIG_BREAD;
use BigBread; 
CREATE TABLE if not exists Recetas (ID_Receta int);
CREATE TABLE if not exists Productos (
id_producto INT not null PRIMARY KEY AUTO_INCREMENT,
Nombre varchar(100) not null,
Descripción varchar(200) not null,
Precio decimal(10,2) not null,
Tipo varchar(100)  not null,
Incluye_promo varchar(20) not null,
ID_Receta int  not null,
ID_Insumos int  not null,
FOREIGN KEY (ID_Receta) REFERENCES Productos(id_producto));
