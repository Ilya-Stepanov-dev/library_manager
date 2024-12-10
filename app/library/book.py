from ..utils.enums import BookStatus
from ..utils.validator import validator
from dataclasses import asdict, dataclass

@dataclass
class Book():
    def __init__(self, 
                 id: int, 
                 title: str, 
                 author: str, 
                 year:int,
                 status: BookStatus = BookStatus.AVAILABLE.value
        ) -> None:

        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


    def __str__(self) -> str:
        return f'book_id: {self.id}\ntitle: {self.title}\nauthor: {self.author}\nyear: {self.year}\nstatus: {self.status}'


    @property
    def id(self) -> int:
        return self._id


    @id.setter
    def id(self, id: int) -> None:
        self._id = validator.validate_id(id)

    
    @property
    def title(self) -> str:
        return self._title


    @title.setter
    def title(self, title: str) -> None:
        self._title = validator.validate_title(title)


    @property
    def author(self) -> str:
        return self._author


    @author.setter
    def author(self, author: str):
        self._author = validator.validate_author(author)


    @property
    def year(self) -> int:
        return self._year
    

    @year.setter
    def year(self, year: int) -> None:
        self._year = validator.validate_year(year)


    @property
    def status(self) -> BookStatus:
        return self._status


    @status.setter
    def status(self, status: BookStatus) -> None:
        self._status = validator.validate_status(status)


    def __str__(self) -> str:
        return f'book_id: {self.id}\ntitle: {self.title}\nauthor: {self.author}\nyear: {self.year}\nstatus: {self.status}'


    # def to_dict(self) -> dict:
    #     return asdict(self)
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }
    

    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return all((self.title.lower() == other.title.lower(),
                       self.author.lower() == other.author.lower(),
                       self.year == other.year,)
                    )
        return False

books = []
book1 = Book(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925)
book2 = Book(2, 'The Gratsby', 'F. Sc Fitzgerald', 1925)
book3 = Book(3, 'The Great Gaty', 'F. Scott Fitzald', 1912)

book4 = Book(4, 'The Gratsby', 'F. Sc Fitzgerald', 1925)

books.append(book1)
books.append(book2)
books.append(book3)

# print(tuple(book for book in books))
# print(book == book4 for book in books)

print(book4 in (book for book in books))
# if any((book == book4 for book in books)):
#     print('True')
    
# book = Book(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925)
# print(book.to_dict())
