from library_management import Library, Book

def test_library_system():
    with Library() as library:

        # library.register_user("mumbi", "adminpass", role="admin")
        # library.register_user("tiff", "userpass")

        user_id, role = library.login_user("mumbi", "adminpass")
        if role == "admin":
            print("Admin logged in successfully.")

        # adding a new book
        # book = Book(title="The River Between", author="Margaret Ogolla", rating=4.5)
        # library.add_book(book, role)
        # anotherBook = Book(title="Caucasian Chalk Circle", author="Berolt Bretch", rating=5.0)
        # library.add_book(anotherBook, role)
        # yetanotherBook = Book(title="Kidagaa Kimemwozea", author="Ken Walibora", rating=3.0)
        # library.add_book(yetanotherBook, role)


        # viewing books
        books = library.view_books()
        print("Books in the library:", books)


        # logging in as a normal user
        user_id, role = library.login_user("tiff", "userpass")
        if role == "user":
           print("User logged in successfully.")


        # trying to add a book as a normal user
        # book = Book(title="Tumbo Lisiloshiba", author="Said Ahmed Mohamed", rating=3.0)
        # library.add_book(book, role)


        # searching for books
        search_results = library.search_books("Berolt Bretch")
        print("Search results:", search_results)


        # borrowing a book
        if library.borrow_book(1):
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")


        # returning a book
        library.return_book(1)
        print("Book returned successfully.")

if __name__ == "__main__":
    test_library_system()
