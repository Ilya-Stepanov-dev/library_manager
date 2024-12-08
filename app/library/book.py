from ..utils.enums import BookStatus
from ..utils.validator import validator

class Book:
    def __init__(self, 
                 id: int, 
                 title: str, 
                 author: str, 
                 year:int,
                 status: BookStatus = BookStatus.AVAILABLE.value
        ) -> None:
        self._id = id
        self._title = title
        self._author = author
        self._year = year
        self._status = status


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


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

