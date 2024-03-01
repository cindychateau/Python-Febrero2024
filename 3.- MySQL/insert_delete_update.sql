SELECT * FROM usuarios;

-- Guardar un nuevo registro en usuarios
INSERT INTO usuarios(nombre, edad, direccion_id) VALUES ('Juana', 18, 3);

-- Eliminar un registro
DELETE FROM usuarios WHERE id = 8;

-- Actualizamos
UPDATE usuarios SET edad = 51 WHERE id = 9;

UPDATE usuarios SET nombre = 'Pablito', edad = 52 WHERE id = 9;
