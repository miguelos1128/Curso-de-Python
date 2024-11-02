from typing import Any


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro '{self.title}' ha sido prestado.")
        else:
            print(f"El libro '{self.title}' ya está prestado.")
    
    def return_book(self):
        self.available = True
        print(f"El libro '{self.title} ha sido devuelto")
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro '{self.title} No esta disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} No esta en la lista de prestados")
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado a la biblioteca.")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado.")
    
    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} por {book.author}")

#Crera Libros
book1 = Book("El principito", "Antonie de Saint Exupery")
book2 = Book("1984", "George Orwell")
book3 = Book("Padre Rico padre pobre", "Robert Kiyosaky")

#Crear Usuario
user1 = User("Miguel Angel", "001")
user2 = User("Maura Oidor", "002")

#Crear Biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_user(user1)
library.register_user(user2)

#Mostrar Libros disponibles
library.show_available_books()

#Realizar prestamo
user1.borrow_book(book3)
user2.borrow_book(book1)

#Mostrar Libros disponibles
library.show_available_books()

#Devolver libro
user1.return_book(book3)

#Mostrar Libros disponibles
library.show_available_books()