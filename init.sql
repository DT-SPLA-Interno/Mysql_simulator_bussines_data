# init.sql - Script de creación de tablas en MySQL
CREATE TABLE operaciones_bancarias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_operacion ENUM('transferencia', 'retiro', 'pago') NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    moneda ENUM('USD', 'EUR', 'PEN') NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cuenta_origen VARCHAR(20),
    cuenta_destino VARCHAR(20),
    estado ENUM('pendiente', 'completado', 'rechazado') NOT NULL
);

CREATE TABLE operaciones_retail (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_operacion ENUM('compra', 'venta') NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    moneda ENUM('USD', 'EUR', 'PEN') NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    estado ENUM('pendiente', 'completado', 'rechazado') NOT NULL
);
