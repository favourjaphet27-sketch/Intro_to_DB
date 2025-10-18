"""This script connects to the mysql server and creates the database alx_book_store. If the database already exists, the script does not fail"""

import mysql.connector
from mysql.connector import Error

try:
    # connect to MYSQL server (no specific database yet)
    connection = mysql.connector.connect(
        host="localhost", user="Japheth", password="tygo9843hy.m"
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MYSQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
