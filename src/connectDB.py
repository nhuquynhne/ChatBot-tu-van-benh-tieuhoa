import mysql.connector
from mysql.connector import MySQLConnection, Error

def connectDB():
    try:
        # Ket noi MySQL voi Python bang ham mysql.connector.connect()
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="btlhtdttt"
        )
        # print("Ket noi thanh cong!")
        return db
    except: # Truong hop co loi khi ket noi
        print("Kiem tra lai thong tin ket noi!")