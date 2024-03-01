-- Desplegando todas las columnas de la tabla usuarios
SELECT * FROM usuarios;

-- Desplegando columna nombre y edad de la tabla usuarios
SELECT nombre, edad FROM usuarios;

-- Desplegando columna id, nombre, edad de la tabla usuarios DONDE el id = 2
SELECT id, nombre, edad FROM usuarios WHERE id = 2;

-- Desplegando todas las columnas de la tabla usuarios DONDE nombre sea "Alejandro"
SELECT * FROM usuarios WHERE nombre LIKE "Alejandro";

-- Desplegando todas las columnas de la tabla usuarios DONDE nombre comience con Al
SELECT * FROM usuarios WHERE nombre LIKE "Al%";

-- Desplegando todas las columnas de la tabla usuarios DONDE nombre termine en o
SELECT * FROM usuarios WHERE nombre LIKE "%o";

-- Despliega nombre y edad de tabla usuarios donde nombre termina con o Y edad es mayor a 2
SELECT nombre, edad FROM usuarios WHERE nombre LIKE "%o" AND edad > 24;

-- Despliega nombre y edad de tabla usuarios donde nombre termina con o O edad es mayor a 2
SELECT nombre, edad FROM usuarios WHERE nombre LIKE "%o" OR edad > 24;

-- Despliega nombre y edad de tabla usuarios donde nombre termina con o O edad es mayor a 2
-- Ordenado por edad ASC (de menor a mayor)
SELECT nombre, edad FROM usuarios WHERE nombre LIKE "%o" OR edad > 24 ORDER BY edad ASC;

-- Despliega nombre y edad de tabla usuarios donde nombre termina con o O edad es mayor a 2
-- Ordenado por nombre DESC (Z-A)
SELECT nombre, edad FROM usuarios WHERE nombre LIKE "%o" OR edad > 24 ORDER BY nombre DESC;