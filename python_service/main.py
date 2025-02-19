# Python Service (python_service/main.py)
import mysql.connector
import random
import time
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host="mysql",
        user="user",
        password="password",
        database="banco_simulacion"
    )

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
    insert_data()
    delete_old_data()
    time.sleep(60)
