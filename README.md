# Guía para Desplegar y Validar el Proyecto

## Requisitos Previos
Antes de iniciar, asegúrate de tener instalado:
- Docker
- Docker Compose

## Pasos para Levantar el Proyecto

1. **Clonar el repositorio o descargar los archivos**
   ```sh
   git clone https://github.com/DT-SPLA-Interno/Mysql_simulator_bussines_data.git
   cd Mysql_simulator_bussines_data
   ```

2. **Construir y levantar los servicios con Docker Compose**
   ```sh
   sudo docker-compose up -d --build
   ```
   Esto iniciará:
   - Un contenedor MySQL con la base de datos preconfigurada.
   - Un servicio en Python que genera datos cada minuto. (puede fallar al primer intento porque el mysql no esta iniciado, pero con validar que el mysql esta corriendo y volver a correr el build todo funcionara)

3. **Verificar que los contenedores están corriendo**
   ```sh
   sudo docker ps
   ```
   Deberías ver al menos dos contenedores: `mysql_db` y `python_service`.

## Validación de la Base de Datos

4. **Acceder a MySQL dentro del contenedor**
   ```sh
   sudo docker exec -it mysql_db mysql -u user -p
   ```
   (Introduce la contraseña: `password`)

5. **Verificar que las tablas existen**
   ```sql
   USE banco_simulacion;
   SHOW TABLES;
   ```
   Debería listar:
   - `operaciones_bancarias`
   - `operaciones_retail`
   - `inventarios`

6. **Comprobar inserciones automáticas**
   ```sql
   SELECT * FROM operaciones_bancarias ORDER BY fecha DESC LIMIT 10;
   SELECT * FROM operaciones_retail ORDER BY fecha DESC LIMIT 10;
   ```
   Deberías ver datos generados automáticamente.

7. **Verificar eliminación de registros antiguos**
   - Espera un par de minutos.
   - Vuelve a ejecutar los comandos anteriores y verifica que los registros más antiguos se eliminan conforme se agregan nuevos.

## Acceso Remoto a la Base de Datos
Para conectarte a la base de datos MySQL desde un cliente remoto, asegúrate de que:
- El host donde está ejecutándose MySQL tiene el **puerto 3306 abierto**.
- MySQL está configurado para aceptar conexiones remotas modificando `bind-address = 0.0.0.0` en su configuración.
- Se ha creado un usuario con acceso desde cualquier IP (`'user'@'%'`).

Para probar la conexión desde un cliente MySQL externo:
```sh
mysql -h <IP_DEL_SERVIDOR> -u user -p
```

## Detener los Contenedores
Para detener la ejecución:
```sh
sudo docker-compose down
```

## Notas
- Si deseas modificar el intervalo de inserción/eliminación, edita `main.py` dentro del servicio Python y cambia `time.sleep(60)` a otro valor en segundos.
- Para volver a iniciar el servicio después de modificaciones:
  ```sh
  sudo docker-compose up -d --build
  ```

¡Listo! Ahora tu simulación de operaciones bancarias y retail está corriendo correctamente. 🚀
