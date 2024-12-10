from enum import Enum

class BookStatus(str, Enum):
    AVAILABLE = 'Available'
    BORROWED = 'Borrowed'

class MenuDesignations(str, Enum):
    EXIT = 'x'
    BACK = 'b'
    SAVE = 's'
    DELETE = 'd'
