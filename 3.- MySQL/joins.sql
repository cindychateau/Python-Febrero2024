SELECT * FROM usuarios;

-- Relacion 1:1
-- Igualo la llave foránea con la llave primaria (FK = PK)
SELECT * FROM usuarios
JOIN direcciones ON usuarios.direccion_id = direcciones.id;

-- Relacion 1:n
SELECT * FROM pedidos
JOIN usuarios ON pedidos.usuario_id = usuarios.id;

-- Relacion n:m
-- 1.- Unimos usuarios con usuarios_has_hobbies usuarios.id = usuarios_has_hobbies.usuario_id
-- 2.- Unimos usuarios_has_hobbies con hobbies usuarios_has_hobbies.hobbie_id = hobbies.id
SELECT nombre, actividad FROM usuarios
JOIN usuarios_has_hobbies ON usuarios_has_hobbies.usuario_id = usuarios.id
JOIN hobbies ON hobbies.id = usuarios_has_hobbies.hobbie_id
WHERE usuarios.id = 2;

SELECT * FROM usuarios
JOIN pedidos ON pedidos.usuario_id = usuarios.id; -- Tenga un pedido el usuario

SELECT * FROM usuarios -- Me aparecen todos los registros de la tabla principal/base
LEFT JOIN pedidos ON pedidos.usuario_id = usuarios.id;
