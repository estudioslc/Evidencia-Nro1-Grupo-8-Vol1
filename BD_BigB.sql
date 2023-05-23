CREATE database BD_BIGBREAD_SA;

USE BD_BIGBREAD_SA;

CREATE table PRODUCTO(
Id_producto int primary key auto_increment, 
Nombre varchar(40) not null, 
Descripcion  varchar(200),
Precio decimal(10,2) not null);


 
 CREATE table INSUMOS( 
 id_insumo int primary key auto_increment,
 Nombre varchar (40) not null,
 descripcion varchar (200)
 );
 
 CREATE table PRODUCCION ( 
 id_produccion int primary key auto_increment,
 id_producto int,
 fecha date not null,
 cantidad int not null,
 foreign key (id_producto) references PRODUCTO(id_producto)
);

CREATE table RECETAS(
id_produccion INT,
id_insumo INT,
cantidad DECIMAL(10, 2) NOT NULL,
FOREIGN KEY (id_produccion) REFERENCES Produccion(id_produccion),
FOREIGN KEY (id_insumo) references INSUMOS(id_insumo)
);



INSERT INTO PRODUCTO (nombre, descripcion, precio) VALUES
  ('pan', 'Producto elaborado a base de harina de trigo', 279.99),
  ('torta', 'Pastel de vainilla relleno de dulce de leche y crema', 3500.50),
  ('tortuguita', 'Sándwich de jamon, queso, tomate y lechuga', 300.00),
  ('masas', 'varierdad de masas secas por kilo', 2500,00),
  ('factura', 'masa dulce individual decorada con crema pastelera', 150,50);
  

INSERT INTO insumos (nombre, descripcion) VALUES
  ('harina', 'polvo base para la elaboracion de masas con tacc'),
  ('agua', 'liquido utilizado para la unión de la masa'),
  ('Pan lomo', 'Base del sándwich tortuguita'),
  ('levadura', 'fermento de la masa para conseguir volumen'),
  ('crema pastelera', 'crema a base de maizena, azucar y manteca'),
  ('Tomate', 'Fruto utilizado como ingrediente en los sándwiches'),
  ('Mayonesa', 'Salsa cremosa utilizada para aderezar el sándwich'),
  ('tomate', 'fruto utilizado en rodajas para sandwich'),
  ('dulce de leche', 'dulce utilizado en variedad de productos' );



INSERT INTO Produccion (id_producto, fecha, cantidad) VALUES
  (1, '2023-04-20', 50),
  (2, '2023-04-20', 10),
  (3, '2023-04-20', 15),
  (4, '2023-04-20', 50),
  (5, '2023-04-20', 100);

