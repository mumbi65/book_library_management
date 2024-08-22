import mysql.connector

def create_database():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Donapple@65"
    )

    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
    print("Database created successfully")

    mydb.close()

def create_tables():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Donapple@65",
        database = "library_db"
    )

    cursor = mydb.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   title VARCHAR(255),
                   author VARCHAR(255),
                   rating FLOAT,
                   is_borrowed BOOLEAN DEFAULT 0
                )
    ''')
    print("Tables created successfully")

    mydb.close()

def create_users():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Donapple@65",
        database = "library_db"
    )

    cursor = mydb.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   username VARCHAR(255)NOT NULL UNIQUE,
                   password VARCHAR(255)NOT NULL,
                   role ENUM('admin', 'user') NOT NULL DEFAULT 'user'
                )
    ''')
    print("Tables created successfully")

    mydb.close()

if __name__ == "__main__":
    create_database()
    create_tables()
    create_users()