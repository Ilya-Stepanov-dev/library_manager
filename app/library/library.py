import json
from .book import Book
from ..utils.data_helper import data_helper as dh
from ..utils.exceptions import *


class Library:
    def __init__(self, path_data: str = 'app/data/', file_name='books.json') -> None:
        self.path_data = path_data
        self.file_name = file_name
        self.books = self._load_books()

    @property
    def data_file(self) -> str:
        """Property that returns the path to the data file."""

        return f'{self.path_data}{self.file_name}'

    def _load_books(self) -> list[Book]:
        """
        Loads books from a json file and returns a list of Book objects.

        The file must be in the following format:
        [
            {
                "id": int,
                "title": str,
                "author": str,
                "year": int,
                "status": str
            },
            ...
        ]

        If the file does not exist or is not in the correct format, an empty list is returned.
        """

        dh.check_data_storage(path_data=self.path_data, file_name=self.file_name)
        try:
            with open(self.data_file, 'r', encoding='utf-8') as fife:
                return [Book(**book) for book in json.load(fife)]
        except json.JSONDecodeError:
            return []

    def _save_books(self) -> None:
        """Saves the list of books to a json file"""

        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)


    def add_book(self, title, author, year) -> Book | None:
        """
        Adds a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year of the book.

        Returns:
            str | None: The id of the book if it is successfully added, otherwise None.

        Raises:
            BookAlreadyExistsError: If a book with the same parameters already exists in the library.
        """

        try:
            book_id = self.books[len(self.books) - 1].id + 1
            new_book = Book(book_id, title, author, year)
            # print(tuple(book for book in self.books))
            if new_book in tuple(book for book in self.books):
            # if any(book.title == new_book.title
            #        and book.author == new_book.author 
            #        and book.year == new_book.year 
            #        for book in self.books):      
                raise BookAlreadyExistsError('A book with these parameters already exists.')
        except IndexError:
            new_book = Book(1, title, author, year)
            self.books.append(new_book)
            self._save_books()
        except Exception as e:
            raise e
        else:
            self.books.append(new_book)
            self._save_books()
        finally:
            return new_book

    def get_all_books(self) -> list[Book] | None:
        """
        Retrieves all books in the library.

        Returns:
            list[Book] | None: A list of all Book objects in the library.
            
        Raises:
            BookNotFound: If no books are found in the library.
        """

        if not self.books:
            raise BookNotFound('Book with this id not found.')
        return self.books

    def remove_book(self, book_id) -> None:
        """
        Removes a book from the library by its ID.

        Args:
            book_id (int): The ID of the book to be removed.

        Raises:
            BookNotFound: If the book with the given ID is not found.
        """

        if book_id == None:
            raise BookNotFound('Book with this id not found.')
        delete_book = self.find_book_id(book_id)
        self.books = [book for book in self.books if book.id != book_id]
        if self.books == []:
            raise BookNotFound('Book with this id not found.')
        self._save_books()
        return delete_book

    def find_books(self, search_term) -> list[Book] | None:
        """
        Finds all books in the library that contain the given search term in their title, author or year.

        Args:
            search_term (str): The search term to search for in the books.

        Returns:
            list[Book] | None: A list of all Book objects that contain the search term in their title, author or year. 
                              If no books are found, raises BookNotFound.
        """

        if not search_term:
            raise BookNotFound('Search term is empty')
        
        books = [book for book in self.books if
                 search_term in (book.title,book.author,str(book.year))]
        
        if not books:
            raise BookNotFound('Book with this id not found.')

        return books

    def find_book_title(self, title) -> list[Book] | None:
        """
        Finds all books in the library with the exact given title.

        Args:
            title (str): The title to search for in the books.

        Returns:
            list[Book] | None: A list of all Book objects with the exact given title. 
                            If no books are found, raises BookNotFound.

        Raises:
            BookNotFound: If the book is not found.
        """

        if title is None:
            raise BookNotFound('Title is None')

        books = [book for book in self.books if title == book.title]
        if books == [] or books is None:
            raise BookNotFound('Book with this id not found.')

        return books

    def find_book_id(self, book_id: int) -> Book | None:
        """
        Finds a book in the library with the exact given id.

        Args:
            book_id (int): The id to search for in the books.

        Returns:
            Book | None: The book object with the exact given id. 
                        If no books are found, raises BookNotFound.

        Raises:
            BookNotFound: If the book is not found.
        """

        if self.books[len(self.books) - 1].id < book_id:
            raise BookNotFound('Invalid book id.')

        book = next((book for book in self.books if book.id == book_id), None)
        if book is None:
            raise BookNotFound('Invalid book id.')

        return book

    def change_status(self, book_id: int, new_status: str) -> Book | None:
        """
        Changes the status of a book in the library with the given id.

        Args:
            book_id (int): The id of the book.
            new_status (str): The new status of the book.

        Returns:
            Book | None: The book object with the new status. 
                        If no books are found, raises BookNotFound.

        Raises:
            BookNotFound: If the book is not found.
        """

        book = self.find_book_id(book_id)
        book.status = new_status
        self._save_books()
        return book
