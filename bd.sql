create database rentaplace;

use rentaplace;

drop table if exists usuarios;

create table usuarios (
id int unsigned not null auto_increment, 
nombre varchar (50) not null, 
correo varchar (50) not null, 
telefono int (10) not null, 
contraseña varchar (50) not null, 
primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;