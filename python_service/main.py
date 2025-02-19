import time
import mysql.connector
import random
from datetime import datetime

def get_connection():
    retries = 10  # Número máximo de intentos
    for i in range(retries):
        try:
            conn = mysql.connector.connect(
                host="mysql",
                user="user",
                password="password",
                database="banco_simulacion"
            )
            print("Conectado a MySQL correctamente.")
            return conn
        except mysql.connector.Error as err:
            print(f"Intento {i+1}/{retries}: No se pudo conectar a MySQL ({err})")
            time.sleep(5)  # Espera 5 segundos antes de intentar nuevamente

    raise Exception("No se pudo conectar a MySQL después de varios intentos")

def insert_data():
    conn = get_connection()
    cursor = conn.cursor()

    for _ in range(10):
        cursor.execute("""
            INSERT INTO operaciones_bancarias (tipo_operacion, monto, moneda, cuenta_origen, cuenta_destino, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            random.choice(['transferencia', 'retiro', 'pago']),
            round(random.uniform(10, 1000), 2),
            random.choice(['USD', 'EUR', 'PEN']),
            f"ACC{random.randint(1000, 9999)}",
            f"ACC{random.randint(1000, 9999)}",
            random.choice(['pendiente', 'completado', 'rechazado'])
        ))

        cursor.execute("""
            INSERT INTO operaciones_retail (tipo_operacion, monto, moneda, producto_id, cantidad, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            random.choice(['compra', 'venta']),
            round(random.uniform(5, 500), 2),
            random.choice(['USD', 'EUR', 'PEN']),
            random.randint(1, 100),
            random.randint(1, 10),
            random.choice(['pendiente', 'completado', 'rechazado'])
        ))
    
    conn.commit()
    conn.close()

def delete_old_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM operaciones_bancarias ORDER BY fecha ASC LIMIT 10")
    cursor.execute("DELETE FROM operaciones_retail ORDER BY fecha ASC LIMIT 10")
    conn.commit()
    conn.close()

while True:
    print("Insertando datos en la base de datos...")
    insert_data()
    print("Eliminando datos antiguos...")
    delete_old_data()
    print("Esperando 60 segundos antes del próximo ciclo...")
    time.sleep(60)
