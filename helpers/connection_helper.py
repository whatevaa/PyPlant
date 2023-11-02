#!/usr/bin/env python

import mysql.connector #from mysql.connector import connect, Error
from mysql.connector import errorcode
import os
from dotenv import load_dotenv
load_dotenv('c:/Projects/PyPlant/.env') # Path to .env file where is store environment variables (ignore by gitignore file)


# To create connection mysql, use of mysql.connector.MySQLConnection() Class, rather than mysql.connector.connect(). 
# Thus we can use later "connection.is_connected()", the function is_connected() of MySQLConnection objects
# Does not seems possible by using the method connect() of the module mysql.connector to create connection => mysql.connector.connect()
def create_server_connection():
    """Create a server connection."""
    connection = None
    try:
        connection = mysql.connector.MySQLConnection( # Rather than mysql.connector.connect()
            host="localhost",
            user= os.environ.get('DB_USER'),
            password= os.environ.get('DB_PASS')
        )
        print(connection)
    except mysql.connector.Error as e:
        print(e)
    return connection


def create_db_connection(db_name):
    """Create a connection to a specifique database and store error number if database does not exist"""
    connection = None
    err = ''
    try:
        connection = mysql.connector.MySQLConnection( # Rather than mysql.connector.connect()
            host="localhost",
            user= os.environ.get('DB_USER'),
            password= os.environ.get('DB_PASS'),
            database= db_name # 'pyplant'
        )
        print(connection)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Wrong user name or password")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist", error.errno)
            err = error.errno
        else:
            print("Error while connecting to MySQL", error)
    return connection, err