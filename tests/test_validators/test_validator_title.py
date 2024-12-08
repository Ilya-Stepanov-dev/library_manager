import unittest

from app.utils.validator import validator
from app.utils.exceptions import InvalidTitleError

class TestValidatorsTitle(unittest.TestCase):
    def test_validate_title_valid(self):
        """Test that validate_title returns the title if it is valid."""

        for title in ['title', 'Title title']:
            with self.subTest(title=title):
                self.assertEqual(validator.validate_title(title), title)
        
    def test_validate_title_is_str(self):
        """Test that validate_title raises an InvalidTitleError if the author is not a string."""

        with self.assertRaises(InvalidTitleError):
            validator.validate_title(123)

    def test_validate_title_is_not_empty(self):
        """Test that validate_title raises an InvalidTitleError if the title is empty."""

        with self.assertRaises(InvalidTitleError):
            validator.validate_title('')

    def test_validate_title_is_min_length(self):
        """Test that validate_title raises an InvalidTitleError if the title is less than 2 characters."""

        with self.assertRaises(InvalidTitleError):
            validator.validate_title('Aa')

    def test_validate_title_is_max_length(self):
        """Test that validate_title raises an InvalidTitleError if the title is more than 50 characters."""

        with self.assertRaises(InvalidTitleError):
            validator.validate_title('abce' * 13)

    def test_validate_title_is_not_repeating_characters(self):
        """Test that validate_title raises an InvalidTitleError if the title contains more than 2 consecutive identical characters."""

        with self.assertRaises(InvalidTitleError):
            validator.validate_title('abvfddde')