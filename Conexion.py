import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establece la conexión con tu base de datos MySQL
        connection = mysql.connector.connect(
            host='localhost',  # o '127.0.0.1'
            user='root',  # Reemplaza con tu usuario de MySQL
            password='contrasena',  # Reemplaza con tu contraseña
            database='terra'  # Reemplaza con el nombre de tu base de datos
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Conectado a la base de datos: {record}")
        
        return connection

    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión MySQL cerrada")

# Llama a la función para conectarte a la base de datos
connection = connect_to_mysql()