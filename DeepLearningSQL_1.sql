CREATE TABLE estudiantes(
    estudiante_id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad TEXT NOT NULL,
    no_carnet INTEGER NOT NULL,
    grado TEXT NOT NULL,
    curso_incrito INTEGER NOT NULL,
    FOREIGN KEY (curso_incrito) REFERENCES cursos(curso_id)
);

CREATE TABLE profesores(
    profesor_id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    estudios TEXT NOT NULL
);

CREATE TABLE administradores(
    administrador_id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    area TEXT NOT NULL
);

CREATE TABLE cursos(
    curso_id INTEGER PRIMARY KEY,
    area TEXT NOT NULL,
    nombre TEXT NOT NULL,
    profesor INTEGER NOT NULL,
    administrador INTEGER NOT NULL,
    FOREIGN KEY (profesor) REFERENCES profesores(profesor_id),
    FOREIGN KEY (administrador) REFERENCES administradores(administrador_id)
    );
  
  -- Insertar datos en la tabla administradores
INSERT INTO administradores (administrador_id, nombre, area) VALUES
(1, 'Juan Perez', 'Recursos Humanos'),
(2, 'Maria Rodriguez', 'Administracion'),
(3, 'Carlos Sanchez', 'Infraestructura');

-- Insertar datos en la tabla profesores
INSERT INTO profesores (profesor_id, nombre, edad, estudios) VALUES
(1, 'Pedro Garcia', 35, 'Licenciatura en Matematicas'),
(2, 'Laura Lopez', 32, 'Licenciatura en Fisica'),
(3, 'David Martinez', 38, 'Licenciatura en Quimica'),
(4, 'John Connor', 38, 'Ingenieria de Sistemas');

-- Insertar datos en la tabla cursos
INSERT INTO cursos (curso_id, area, nombre, profesor, administrador) VALUES
(1, 'Matematicas', 'Algebra', 1, 1),
(2, 'Fisica', 'Mecanica', 2, 2),
(3, 'Quimica', 'Quimica Organica', 3, 3);

  INSERT INTO estudiantes (estudiante_id, nombre, edad, no_carnet, grado, curso_incrito) VALUES
(1, 'Ricardo Pulido', 21, 45687, "primero", 002),
(2, 'Jordy Bautista', 28, 13564, "segundo", 001),
(3, 'Jessica Munoz', 19, 2226547, "primero", 002),
(4, 'Elon musk', 15, 98654, "segundo", 005),
(5, 'Mark Zukerberg', 55, 874954, "segundo", 007);

/*Tipos de JOIN*/
-- Solo los cursos y que tienen administradores
SELECT cursos.nombre, administradores.nombre
FROM cursos
INNER JOIN administradores ON cursos.administrador = administradores.administrador_id;

-- Todos los estudiantes y el curso en el que esta (no importa si no tiene curso)
SELECT estudiantes.nombre, cursos.nombre
FROM estudiantes
LEFT JOIN cursos ON estudiantes.curso_incrito = cursos.curso_id;

-- Todos los cursos y si tienen profesores que los dictan
SELECT cursos.nombre, profesores.nombre
FROM cursos
RIGHT JOIN profesores ON cursos.curso_id = profesores.profesor_id;

-- Todos los cursos y estudiantes si hay por lo menos un curso con estudiantes
SELECT estudiantes.nombre, cursos.nombre
FROM estudiantes
FULL JOIN cursos ON estudiantes.curso_incrito = cursos.curso_id;

/*Consulta con where*/
-- Todos los estudiantes que tengan mas de 18 años y esten en grado primero
SELECT *
FROM estudiantes
WHERE edad > 18 AND grado = "primero";

-- Todos los profesores que estudiaron una Licenciatura 
SELECT *
FROM profesores
WHERE estudios LIKE "%Licenciatura%";
