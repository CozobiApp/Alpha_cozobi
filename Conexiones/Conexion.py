import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        
        connection = mysql.connector.connect(
            host='localhost', 
            user='root',  
            password='contrasena',  
            database='terra'  
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


connection = connect_to_mysql()