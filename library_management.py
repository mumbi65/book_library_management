import mysql.connector

class Book:
    def __init__(self, title, author, rating, is_borrowed=False):
        self.title = title
        self.author = author
        self.rating = rating
        self.is_borrowed = is_borrowed

class Library:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Donapple@65",
                database = "library_db"
            )
            self.cursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            raise

    def add_book(self, book, role):
        if role != 'admin':
            print("Permission denied. Only admins can add books.")
            return
        query = "INSERT INTO books(title, author, rating, is_borrowed) VALUES(%s, %s, %s, %s)"
        values = (book.title, book.author, book.rating, book.is_borrowed)
        self.cursor.execute(query, values)
        self.mydb.commit()
        print("Book added successfully.")

    def view_books(self, sort_by = 'title', limit = None):
        query = f"SELECT * FROM books ORDER BY {sort_by}"
        if limit:
            query += f"LIMIT {limit}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def search_books(self, keyword):
        query = "SELECT * FROM books WHERE LOWER(title) LIKE LOWER(%s) OR LOWER(author) LIKE LOWER(%s)"
        values = ('%' + keyword + '%', '%' + keyword + '%')
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    def borrow_book(self, book_id):
        check_query = "SELECT is_borrowed FROM books WHERE id = %s"
        self.cursor.execute(check_query, (book_id,))
        result = self.cursor.fetchone()
        if result and not result[0]:
            query = "UPDATE books SET is_borrowed = %s WHERE id = %s"
            self.cursor.execute(query, (True, book_id))
            self.mydb.commit()
            return True
        return False
    
    def return_book(self, book_id):
        query = "UPDATE books SET is_borrowed = %s WHERE id = %s"
        self.cursor.execute(query, (False, book_id),)
        self.mydb.commit()

    def get_book(self, book_id):
        query = "SELECT * FROM books WHERE id = %s"
        self.cursor.execute(query, (book_id))
        return self.cursor.fetchone()
    
    def update_book(self, book_id, title, author, rating, role):
        if role != 'admin':
            print("Permission denied. Only admins can update books.")
            return
        query = "UPDATE books SET title = %s, author = %s, rating = %s WHERE id = %s"
        self.cursor.execute(query, (title, author, rating, book_id))
        self.mydb.commit()
        print("Book updated successfully.")

    def delete_book(self, book_id, role):
        if role != 'admin':
            print("Permission denied. Only admins can delete books.")
            return
        query = "DELETE FROM books WHERE id = %s"
        self.cursor.execute(query, (book_id,))
        self.mydb.commit()
        print("Book deleted successfully.")

    def register_user(self, username, password, role='user'):
        query = "INSERT INTO users(username, password, role) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (username, password, role))
        self.mydb.commit()

    def login_user(self, username, password):
        query = "SELECT id, role FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, password))
        result = self.cursor.fetchone()
        if result:
            user_id, role = result
            print(f"Login successful. User role: {role}")
            return user_id, role
        else:
            print("Login failed. Incorrect username or password.")
            return None

    def close_connection(self):
        self.cursor.close()
        self.mydb.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()