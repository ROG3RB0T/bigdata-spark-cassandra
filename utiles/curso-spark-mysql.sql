-- base de datos prueba para curso big data spark
-- Rodrigo Alfaro, ralf@netstream.cl

CREATE TABLE `clientes` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`nombre` varchar(50) DEFAULT NULL,
`apellidos` varchar(50) DEFAULT NULL,
`genero` tinyint(2) DEFAULT 0, -- 0 Masculino 1 Femenino
`edad` tinyint(4) DEFAULT 0,
PRIMARY KEY (`ID`)
);
-- insert
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Rodrigo', 'Alfaro Pinto', 0, 36);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Jhon', 'Doe Espinoza', 0, 22);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Safiyyah', 'Mccarthy', 1, 13);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Norma', 'Donnelly', 1, 34);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Poppie', 'Bush', 1, 55);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Bridget', 'Walters', 1, 11);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Ella-Mae', 'Farmer', 1, 18);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Skyla', 'Wolf', 1, 21);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Tania', 'Morgan', 1, 22);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Katherine', 'Richardson', 1, 23);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Blanche', 'Steele', 1, 23);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Finley', 'Spence', 0, 21);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Elisabeth', 'Jensen', 1, 22);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Martha', 'Adams', 1, 55);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Kylie', 'Reese', 1, 16);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Caitlyn', 'Barnett', 1, 17);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Shelby', 'Thompson', 1, 18);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Aleksandra', 'Allen', 1, 19);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Marwa', 'Conner', 1, 20);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Kendra', 'Thomas', 1, 21);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Remi', 'Jackson', 1, 22);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Nia', 'Mendoza', 1, 22);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Evie-Mae', 'Daniels', 1, 21);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Diana', 'Ford', 1, 34);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Dianne', 'Barker', 1, 67);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Joe', 'Lewis', 0, 15);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Charles', 'Torres', 0, 44);
INSERT INTO clientes (nombre, apellidos, genero, edad) VALUES ('Chris', 'Hodges', 0, 36);
