
__all__ = ['BaseExceptionApp', 
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


class BaseExceptionApp(Exception):    
    def __init__(self, message: str, *args: object) -> None:
        super().__init__()
        self.message = message
        self.args = args

    def __str__(self) -> str:
        if not self.args or not self.args[0]:
            return f'{self.__class__.__name__}: {self.message}\n'
        
        args_str = '\n'.join(str(arg) for arg in self.args)
        return f'{self.__class__.__name__}: {self.message}\n{args_str}\n'


class InvalidIDError(BaseExceptionApp):
    pass


class InvalidTextError(BaseExceptionApp):
    pass


class InvalidAuthorError(BaseExceptionApp):
    pass


class InvalidTitleError(BaseExceptionApp):
    pass


class InvalidYearError(BaseExceptionApp):
    pass


class InvalidStatusError(BaseExceptionApp):
    pass

    
class BookNotFound(BaseExceptionApp):
    pass


class StatusNotFound(BaseExceptionApp):
    pass


class BookAlreadyExistsError(BaseExceptionApp):
    pass
