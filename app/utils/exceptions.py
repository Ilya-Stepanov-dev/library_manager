
__all__ = ['BaseException', 
           'InvalidIDError', 
           'InvalidTextError',
           'InvalidTitleError',
           'InvalidAuthorError', 
           'InvalidYearError', 
           'InvalidStatusError',
           'BookNotFound',
           'StatusNotFound',
           'BookAlreadyExistsError',
]


class BaseException(Exception):    
    def __init__(self, message: str, *args: object) -> None:
        super().__init__()
        self.message = message
        self.args = args

    def __str__(self) -> str:
        if not self.args or not self.args[0]:
            return f'{self.__class__.__name__}: {self.message}\n'
        
        args_str = '\n'.join(str(arg) for arg in self.args)
        return f'{self.__class__.__name__}: {self.message}\n{args_str}\n'


class InvalidIDError(BaseException):
    pass


class InvalidTextError(BaseException):
    pass


class InvalidAuthorError(BaseException):
    pass


class InvalidTitleError(BaseException):
    pass


class InvalidYearError(BaseException):
    pass


class InvalidStatusError(BaseException):
    pass

    
class BookNotFound(BaseException):
    pass


class StatusNotFound(BaseException):
    pass


class BookAlreadyExistsError(BaseException):
    pass
