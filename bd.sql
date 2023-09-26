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

CREATE TABLE propiedades (
    ID INT NOT NULL AUTO_INCREMENT,
    ID_dueno INT NOT NULL,
    Titulo VARCHAR(255) NOT NULL,
    Descripcion TEXT,
    Categoria VARCHAR(50),
    Precio DECIMAL(10, 2),
    Metros2 DECIMAL(10, 2),
    Direccion VARCHAR(255),
    NoHabitaciones INT,
    NoSalas INT,
    NoBanios INT,
    NoPersonas INT,
    ZonaEstado VARCHAR(50),
    Antiguedad INT,
    Estado ENUM('Disponible', 'No Disponible'),
    Amueblada ENUM('Si', 'No'),
    Cochera ENUM('Si', 'No'),
    WIFI ENUM('Si', 'No'),
    Television ENUM('Si', 'No'),
    Refrigeradora ENUM('Si', 'No'),
    Fotos TEXT,
    FechaCreacion DATE DEFAULT (CURRENT_DATE),
    PRIMARY KEY (ID),
    KEY ID_dueno (ID_dueno),
    FOREIGN KEY (ID_dueno) REFERENCES usuarios(id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO propiedades (ID_dueno, Titulo, Descripcion, Categoria, Precio, Metros2, Direccion, NoHabitaciones, NoSalas, NoBanios, NoPersonas, ZonaEstado, Antiguedad, Estado, Amueblada, Cochera, WIFI, Television, Refrigeradora, Fotos)
VALUES (1, 'Casa en Hermosillo', 'Espaciosa casa en el corazón de Hermosillo, Sonora', 'Casa', 35000.00, 250.00, 'Calle Ejemplo 123, Colonia Ejemplo', 4, 2, 3, 6, 'Sonora', 12, 'Disponible', 'Si', 'Si', 'Si', 'Si', 'Si', 'https://axxiona.mx/hermosillo/img/entrega1.jpg');

INSERT INTO propiedades (ID_dueno, Titulo, Descripcion, Categoria, Precio, Metros2, Direccion, NoHabitaciones, NoSalas, NoBanios, NoPersonas, ZonaEstado, Antiguedad, Estado, Amueblada, Cochera, WIFI, Television, Refrigeradora, Fotos)
VALUES (1, 'Casa de playa en Puerto Peñasco', 'Amplia casa de playa con vista al mar en Puerto Peñasco', 'Casa', 45000.00, 300.00, 'Calle Playa 456, Fraccionamiento Costero', 3, 2, 2, 8, 'Sonora', 8, 'Disponible', 'Si', 'Si', 'Si', 'Si', 'Si', 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/271435932.jpg?k=41572beb90be04f4afebeb652e06d615cd8d4b68804603d6b4e3d168629a8334&o=&hp=1');

INSERT INTO propiedades (ID_dueno, Titulo, Descripcion, Categoria, Precio, Metros2, Direccion, NoHabitaciones, NoSalas, NoBanios, NoPersonas, ZonaEstado, Antiguedad, Estado, Amueblada, Cochera, WIFI, Television, Refrigeradora, Fotos)
VALUES (1, 'Apartamento en Ciudad Obregón', 'Moderno apartamento en el centro de Ciudad Obregón', 'Apartamento', 22000.00, 120.00, 'Avenida Principal 789, Centro', 2, 1, 1, 3, 'Sonora', 5, 'Disponible', 'No', 'No', 'Si', 'No', 'Si', 'https://cerca-del-imss-depa-otancahuiberna-facturable-ciudad-obregon.booked.mx/data/Photos/OriginalPhoto/12490/1249087/1249087324/Cerca-Del-Imss-Depa-Otancahuiberna-Apartment-Ciudad-Obregon-Exterior.JPEG');

INSERT INTO propiedades (ID_dueno, Titulo, Descripcion, Categoria, Precio, Metros2, Direccion, NoHabitaciones, NoSalas, NoBanios, NoPersonas, ZonaEstado, Antiguedad, Estado, Amueblada, Cochera, WIFI, Television, Refrigeradora, Fotos)
VALUES (1, 'Casa en la Sierra de Sonora', 'Encantadora casa en la Sierra de Sonora con hermosas vistas', 'Chalet', 38000.00, 220.00, 'Camino a la Montaña, Ejido Rural', 3, 2, 2, 6, 'Sonora', 10, 'Disponible', 'Si', 'Si', 'Si', 'Si', 'Si', 'https://cdn1.es.casasrurales.net/emp/fotoscasas/5/4/0/3/2/tb_Fachada%20con%20terraza.jpg');
