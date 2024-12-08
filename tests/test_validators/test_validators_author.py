import unittest

from app.utils.validator import validator
from app.utils.exceptions import InvalidAuthorError

class TestValidatorsAuthor(unittest.TestCase):

    def test_validate_author_valid(self):
        """Test that validate_author returns the author if it is valid."""

        for author in ['author', 'Author author']:
            with self.subTest(author=author):
                self.assertEqual(validator.validate_author(author), author)

    def test_validate_author_is_str(self):
        """Test that validate_author raises an InvalidAuthorError if the author is not a string."""

        with self.assertRaises(InvalidAuthorError):
            validator.validate_author(123)

    def test_validate_author_is_not_empty(self):
        """Test that validate_author raises an InvalidAuthorError if the author is empty."""

        with self.assertRaises(InvalidAuthorError):
            validator.validate_author('')
        
    def test_validate_author_is_min_length(self):
        """Test that validate_author raises an InvalidAuthorError if the author is less than 2 characters."""

        with self.assertRaises(InvalidAuthorError):
            validator.validate_author('Aa')

    def test_validate_author_is_max_length(self):
        """Test that validate_author raises an InvalidAuthorError if the author is more than 50 characters."""

        with self.assertRaises(InvalidAuthorError):
            validator.validate_author('abce' * 13)

    def test_validate_author_is_not_repeating_characters(self):
        """Test that validate_author raises an InvalidAuthorError if the author contains more than 2 consecutive identical characters."""

        with self.assertRaises(InvalidAuthorError):
            validator.validate_author('abvfddde')

    def test_validate_author_is_alpha(self):
        """Test that validate_author raises an InvalidAuthorError if the author contains non-alphabetic characters."""

        with self.assertRaises(InvalidAuthorError):
            validator.validate_author('abc123')


    

    