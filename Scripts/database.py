import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values

secrets = dotenv_values("shhh.env")

def create_db_connection(host, user, password, database):
    print('attempting to connect')
    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if db_connection.is_connected():
            print("Connected to the database")
            return db_connection
        else:
            print("Failed to connect to the database")
            return None  # Return None when the connection fails

    except Error as e:
        print("Error connecting to the database:", e)
        return None

# Call the function with the correct password access
db_connection = create_db_connection(
    host='localhost',
    user='test_server',
    password=secrets['db_password'],
    database='shirts_db'
)
