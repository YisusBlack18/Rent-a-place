CREATE DATABASE IF NOT EXISTS rentaaplace;

CREATE TABLE usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO usuarios (nombre, telefono, email, password) VALUES ('prueba', '6621000000', 'prueba@gmail.com', 'prueba123');
