import mysql.connector

# Replace these values with your actual MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'chen liconga',
    'database': 'mydb'
}


def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return conn
    except:
        return None