CREATE DATABASE BigBread;
USE BigBread;
CREATE TABLE Productos (
  Id_producto int auto_increment not null,
  Nombre varchar (100) not null,
  Descripción varchar (200),
  Precio decimal (10, 2),
  Tipo varchar (100),
  Incluye_promo varchar (20),
  primary key (Id_producto)
);
USE BigBread;
CREATE TABLE Ingredientes(
  id_ingrediente int auto_increment not null,
  Nombre varchar (100),
  Descripción varchar (200),
  Contiene_alérgeno varchar (30),
  Cantidad varchar (100),
  primary key (id_ingrediente)
);
USE BigBread;
CREATE TABLE Recetas(
  Id_receta int auto_increment not null,
  fk_producto int,
  fk_ingrediente int,
  Orden_de_incorpotación int,
  primary key (Id_receta),
  FOREIGN KEY (fk_producto) REFERENCES Productos (Id_producto),
  FOREIGN KEY (fk_ingrediente) REFERENCES Ingredientes (Id_ingrediente)
);

USE BigBread;
CREATE TABLE Cliente (
  Id_cliente int auto_increment not null, 
  Nombre varchar (30),
  Telefono int, 
  Direccion varchar(50), 
  Contiene_bonus varchar (50),
  primary key (Id_cliente)
);

USE BigBread;
CREATE TABLE Tipo_Pago (
  id_Tipopago int auto_increment not null,
  Efectivo int,
  Débito int,
  Crédito int,
  Gift_Card varchar(10),
  primary key (id_Tipopago)
);

USE BigBread;
CREATE TABLE Pedidos (
  Id_pedido int auto_increment not null, 
  fk_producto int,
  fk_cliente int,
  Fecha Date,
  Cantidad int,
  fk_tipo_pago int,
  primary key (Id_pedido),
  FOREIGN KEY (fk_producto) REFERENCES Productos (Id_producto),
  FOREIGN KEY (fk_cliente) REFERENCES Cliente (id_cliente),
  FOREIGN KEY (fk_tipo_pago) REFERENCES Tipo_Pago(id_Tipopago)
);
