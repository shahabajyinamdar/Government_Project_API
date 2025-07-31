import psycopg2
import mysql.connector









def connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "",
            database = "governmentproject",
           
        )
        return conn
    except Exception as e:
        print(e)


    