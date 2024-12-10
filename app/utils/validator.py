from datetime import datetime
from utils.enums import BookStatus
from utils.exceptions import (InvalidYearError, 
                              InvalidIDError, 
                              InvalidTitleError, 
                              InvalidAuthorError, 
                              InvalidStatusError,
)

class Validator:

    def _user_enter(self, arg: object) -> str:
        return f'You enter: {arg}'

    def _validate_int(self, arg: object, exceptions: Exception, name_arg: str) -> int | None:
        """
        Validates the argument as a positive integer.
        
        Args:
            arg (object): The argument to be validated.
            exceptions (Exception): The exception to be raised if validation fails.
            name_arg (str): The name of the argument to be used in exception messages.
        
        Returns:
            int | None: The validated integer if it is positive, or None if validation fails.
        """
        
        try:
            arg = int(arg)
        except Exception as e:
            raise exceptions(f'{name_arg} must be an integer.', self._user_enter(arg))
        
        if arg <= 0:
            raise exceptions(f'{name_arg} must be a positive integer.', self._user_enter(arg))
        
        return arg
    
    def validate_year(self, year: object) -> int | None:
        """
        Validates the argument as a positive integer representing a year.

        Args:
            year (object): The argument to be validated.

        Returns:
            int | None: The validated year if it is a positive integer, or None if validation fails.

        Raises:
            InvalidYearError: If the year is less than 1455 or greater than the current year.
        """
        
        year = self._validate_int(arg=year, exceptions=InvalidYearError, name_arg="Year")

        if year < 1455:   
            raise InvalidYearError('Year must not be less than 1455.', self._user_enter(year), 
                                   '\n(Historical background: In 1455, Gutenberg produced the first full-length printed book, '
                                   'known as the Gutenberg Bible or the 42-line Bible. This was the first work of printing)')

        if year > datetime.now().year:
            raise InvalidYearError('Year must not be greater than current year.', self._user_enter(year), 
                                   f'Current year: {datetime.now().year}')
        return year

    def validate_id(self, id) -> int | None:      
        return self._validate_int(arg=id, exceptions=InvalidIDError, name_arg='ID')
    
    def _validate_rep_characters(self, arg: str, light: int, exceptions: Exception, message: str) -> None:
        """
        Checks if there are any repeating characters in the argument.

        Args:
            arg (str): The argument to be validated.
            light (int): The number of characters to check.
            exceptions (Exception): The exception to be raised if a repeating character is found.
            message (str): The message to be displayed if a repeating character is found.
        """
        
        for i in range(len(arg) - light):
            if all(arg[i] == arg[j] for j in range(i + 1, i + light + 1)):
                raise exceptions(message, self._user_enter(arg))
    

    def _validate_str(self, arg: object, validable_arg: str, min_length: int, max_length: int, exceptions: Exception) -> str | None:
        """
        Validates the argument as a string within specified length constraints and without
        repeating characters.

        Args:
            arg (object): The argument to be validated.
            validable_arg (str): The name of the argument for exception messages.
            min_length (int): The minimum allowed length of the string.
            max_length (int): The maximum allowed length of the string.
            exceptions (Exception): The exception to be raised if validation fails.

        Returns:
            str | None: The validated string if it meets all criteria, or None if validation fails.

        Raises:
            exceptions: If the string is not valid, based on type, length, or repeating character constraints.
        """

        if not isinstance(arg, str) or not arg:
            raise exceptions(f'The {validable_arg} must be a non-empty string.', self._user_enter(arg))
        
        if len(arg) < min_length:
            raise exceptions(f'The {validable_arg} is too short, less than {min_length} characters', self._user_enter(arg))
        
        if len(arg) > max_length:
            raise exceptions(f'The {validable_arg} is too long, more than {max_length} characters', self._user_enter(arg))
        
        self._validate_rep_characters(arg=arg, light=2, exceptions=exceptions, 
                                      message=f'The {validable_arg} must not contain more than {2} identical consecutive characters.')
        
        return arg
    

    def validate_title(self, title: str) -> str | None:
        return self._validate_str(arg=title, validable_arg='Title', min_length=3, max_length=30, exceptions=InvalidTitleError)


    def validate_author(self, author: str) -> str | None:
        """
        Validates the author as a string within specified length constraints, containing only letters or spaces
        and without repeating characters.

        Args:
            author (str): The author to be validated.

        Returns:
            str | None: The validated author if it meets all criteria, or None if validation fails.

        Raises:
            InvalidAuthorError: If the author is not valid, based on type, length, repeating character constraints or contains non-letter characters.
        """

        self._validate_str(arg=author, validable_arg='Author', min_length=3, max_length=30, exceptions=InvalidAuthorError)


        allowed_characters = {' ','.', "'",'-', '&', '/'}
        if not all(char.isalpha() or char in allowed_characters for char in author):
            list_error = [char for char in author if not (char.isalpha() or char in allowed_characters)]
            raise InvalidAuthorError(f'The Author must contain only letters.', self._user_enter(author), f'Invalid characters: {list_error}')
        
        return author


    def validate_status(self, status: BookStatus) -> BookStatus | None:       
        """
        Validates the status as a string within the predefined set of valid statuses.

        Args:
            status (BookStatus): The status to be validated.

        Returns:
            BookStatus | None: The validated status if it is one of the valid statuses, or None if validation fails.

        Raises:
            InvalidStatusError: If the status is not one of the predefined valid statuses.
        """
        
        if status not in [s.value for s in BookStatus]:
            raise InvalidStatusError(f'Status must be one of {", ".join([s.value for s in BookStatus])}.')
        return status
    
validator = Validator()