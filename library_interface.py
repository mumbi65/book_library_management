from tkinter import *
from library_management import Library, Book

library = Library()


root = Tk()

root.title("Login")

root.geometry("500x500")
root.config(bg="lightgrey")

welcome_label = Label(root, text="Welcome", fg="black", font=("Helvitica", 30, 'bold'), bg='lightgrey')
welcome_label.grid(row=0, column=0, pady=45, padx=20, columnspan=5)

def userWindow():
    users_window = Tk()
    users_window.title("User Dashboard")
    users_window.geometry('800x600')

    def view_books():
        books = library.view_books()
        books_list = "\n".join([f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Rating: {book[3]}, Borrowed: {book[4]}" for book in books])
        Label(users_window, text=books_list, justify=LEFT).grid(row=4, column=0, columnspan=2)

    def borrow_book():
        book_id = int(book_id_entry.get())
        success = library.borrow_book(book_id)
        if success:
            message_label.config(text="Book borrowed successfully!", fg="green")
        else:
            message_label.config(text="Failed to borrow the book. It may already be borrowed.", fg="red")

    def return_book():
        book_id = int(book_id_entry.get())
        library.return_book(book_id)
        message_label.config(text="Book returned successfully!", fg="green")

    def get_book_details():
        book_id = int(book_id_entry.get())
        book = library.get_book(book_id)
        if book:
            book_details = f"ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nRating: {book[3]}\nBorrowed: {'Yes' if book[4] else 'No'}"
            book_details_label.config(text=book_details, justify=LEFT)
        else:
            book_details_label.config(text="Book not found.", fg="red")

    Label(users_window, text="User Dashboard", font=("Arial", 24)).grid(row=0, column=0, pady=20, columnspan=2)


    Label(users_window, text="Enter Book ID:").grid(row=1, column=0, padx=10, pady=5)
    book_id_entry = Entry(users_window, width=20)
    book_id_entry.grid(row=1, column=1, padx=10, pady=5)

    borrow_button = Button(users_window, text="Borrow Book", command=borrow_book, width=15)
    borrow_button.grid(row=2, column=0, padx=10, pady=5)

    return_button = Button(users_window, text="Return Book", command=return_book, width=15)
    return_button.grid(row=2, column=1, padx=10, pady=5)

    view_books_button = Button(users_window, text="View All Books", command=view_books, width=15)
    view_books_button.grid(row=3, column=0, padx=10, pady=5)

    book_details_label = Label(users_window, text="", font=('Arial', 15), wraplength=500)
    book_details_label.grid(row=4, column=0, columnspan=2, pady=20)

    

    message_label = Label(users_window, text="", font=('Arial', 12))
    message_label.grid(row=5, column=0, columnspan=2)

    users_window.mainloop()

def adminWindow():
    admin_window = Tk()
    admin_window.title("Admin Panel")
    admin_window.geometry('800x600')

    def add_book():
        title = title_entry.get()
        author = author_entry.get()
        rating = float(rating_entry.get())
        book = Book(title, author, rating)
        library.add_book(book, role='admin')
        message_label.config(text="Book added successfully!", fg="green")

    def update_book():
        book_id = int(book_id_entry.get())
        title = title_entry.get()
        author = author_entry.get()
        rating = float(rating_entry.get())
        library.update_book(book_id, title, author, rating, role="admin")
        message_label.config(text="Book updated successfully!", fg="green")

    def delete_book():
        book_id = int(book_id_entry.get())
        library.delete_book(book_id, role="admin")
        message_label.config(text="Book deleted successfully!", fg="green")

    def view_books():
        books = library.view_books()
        books_list = "\n".join([f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Rating: {book[3]}, Borrowed: {book[4]}" for book in books])
        Label(admin_window, text=books_list, justify=LEFT).grid(row=7, column=0, columnspan=2)


    Label(admin_window, text="Admin Dashboard", font=("Arial", 24, "bold")).grid(row=0, column=0, pady=20, columnspan=2,)

    title_label = Label(admin_window, text="Title:", font=("Arial", 18))
    title_label.grid(row=1, column=0, padx=20, pady=10, sticky=E)
    title_entry = Entry(admin_window, width=30, font=("Arial", 18))
    title_entry.grid(row=1, column=1, padx=20, pady=10)

    author_label = Label(admin_window, text="Author:", font=("Arial", 18))
    author_label.grid(row=2, column=0, pady=10, padx=20, sticky=E)
    author_entry = Entry(admin_window, width=30, font=("Arial", 18))
    author_entry.grid(row=2, column=1, padx=20, pady=10)

    rating_label = Label(admin_window, text="Rating:",font=("Arial", 18))
    rating_label.grid(row=3, column=0, padx=20, pady=10, sticky=E)
    rating_entry = Entry(admin_window, width=30, font=("Arial", 18))
    rating_entry.grid(row=3, column=1, padx=20, pady=10)

    book_id_label = Label(admin_window, text="Book ID:",font=("Arial", 18))
    book_id_label.grid(row=4, column=0, padx=20, pady=10, sticky=E)
    book_id_entry = Entry(admin_window, width=30, font=("Arial", 18))
    book_id_entry.grid(row=4, column=1, padx=20, pady=10)

    add_button = Button(admin_window, text="Add Book", command=add_book)
    add_button.grid(row=5, column=0, padx=20, pady=20)

    update_button = Button(admin_window, text="Update Book", command=update_book)
    update_button.grid(row=5, column=1, padx=20, pady=20)

    delete_button = Button(admin_window, text="Delete Book", command=delete_book)
    delete_button.grid(row=6, column=1, padx=20, pady=20)

    view_books_button = Button(admin_window, text="View All Books", command=view_books)
    view_books_button.grid(row=6, column=0, padx=20, pady=20)

    message_label = Label(admin_window, text="")
    message_label.grid(row=8, column=0, columnspan=2)

    admin_window.mainloop()

def login(role):
    login_window = Tk()
    login_window.title(f'{role.capitalize()} Login')
    login_window.geometry('700x600')

    login_label = Label(login_window, text='Login', font=('Helvitica', 20, "bold" ), fg='black')
    login_label.grid(row=0, column=0, pady=20, padx=20, columnspan=2)

    username_label = Label(login_window, text='Username: ', font=('Arial', 20), fg='black')
    username_label.grid(column=0, row=1, padx=20, pady=20)

    username_entry = Entry(login_window, width=30, font=('Arial', 20))
    username_entry.grid(column=1, row=1)

    password_label = Label(login_window, text='Password: ', font=('Arial', 20), fg='black')
    password_label.grid(column=0, row=2, padx=20, pady=20)

    password_entry = Entry(login_window, width=30, font=('Arial', 20))
    password_entry.grid(column=1, row=2)

    def login_action():
        user_info = library.login_user(username_entry.get(), password_entry.get())
        if user_info:
            user_id, role_from_db = user_info
            if role == 'user' and role_from_db == 'user':
                userWindow()
            elif role == 'admin' and role_from_db == 'admin':
                adminWindow()
            else:
                message_label.config(text="Invalid role for this login", fg='red')
        else:
            message_label.config(text="Login failed. Try again.", fg='red')

    submit_button = Button(login_window, text='Login', command=login_action)
    submit_button.grid(column=1, row=4)

    message_label = Label(login_window, text='', fg='red', font=('Arial', 15))
    message_label.grid(column=1, row=5, pady=20)

    root.destroy()

    login_window.mainloop()

def register():
    register_window = Tk()
    register_window.title('Register')
    register_window.geometry('700x600')

    register_label = Label(register_window, text='Register', font=('Helvitica', 30, "bold" ), fg='black')
    register_label.grid(row=0, column=0, pady=20, padx=20, columnspan=2)

    username_label = Label(register_window, text='Username: ', font=('Arial', 20), fg='black')
    username_label.grid(column=0, row=1, padx=20, pady=20)

    username_entry = Entry(register_window, width=30, font=('Arial', 20))
    username_entry.grid(column=1, row=1)

    password_label = Label(register_window, text='Password: ', font=('Arial', 20), fg='black')
    password_label.grid(column=0, row=2, padx=20, pady=20)

    password_entry = Entry(register_window, width=30, font=('Arial', 20))
    password_entry.grid(column=1, row=2)

    confirm_password_label = Label(register_window, text='Confirm Password: ', font=('Arial', 20), fg='black')
    confirm_password_label.grid(column=0, row=3, padx=20, pady=20)

    confirm_password_entry = Entry(register_window, width=30, font=('Arial', 20))
    confirm_password_entry.grid(column=1, row=3)

    role_label = Label(register_window, text='Role: ', font=('Arial', 20), fg='black')
    role_label.grid(column=0, row=4, padx=20, pady=20)

    role_var = StringVar()
    role_var.set('user')

    role_dropdown = OptionMenu(register_window, role_var, 'user', 'admin')
    role_dropdown.config(width=30, font=('Arial', 20))
    role_dropdown.grid(column=1, row=4)

    def submit_registration():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        role = role_var.get()

        if password == confirm_password:
            library.register_user(username, password, role)
            print(f"Registered as {role}")
            register_window.destroy()
        else:
            error_label.config(text="Passwords do not match!", fg='red')

    submit_button = Button(register_window, text='Submit', command=submit_registration)
    submit_button.grid(column=1, row=5)

    error_label = Label(register_window, text='', font=('Arial', 15))
    error_label.grid(column=1, row=6)

    root.destroy()

    register_window.mainloop()



user_login_button = Button(root, text='User Login', command=lambda: login('user'))
user_login_button.grid(row=1, column=0)

admin_login_button = Button(root, text='Admin Login', command=lambda: login('admin'))
admin_login_button.grid(row=1, column=1)

register_button = Button(root, text='Register', command=register)
register_button.grid(row=1, column=2)
root.mainloop()