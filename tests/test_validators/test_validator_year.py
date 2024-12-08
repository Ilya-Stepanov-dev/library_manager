import unittest 

from app.utils.validator import validator
from app.utils.exceptions import InvalidYearError
from datetime import datetime

class TestValidatorsYear(unittest.TestCase):
    def test_validate_year_valid(self):
        """Test that validate_year returns the year if it is valid."""
        
        for year in [1594, '1876', datetime.now().year]:
            with self.subTest(year=year):
                self.assertEqual(validator.validate_year(year), int(year))
    
    def test_validate_year_invalid(self):
        """Test that validate_year raises an InvalidYearError if the year is invalid."""
        
        for year in ['14345',12341, '432', 143]:
            with self.assertRaises(InvalidYearError):
                validator.validate_year(year)

    def test_validate_year_negative(self):
        """Test that validate_year raises an InvalidYearError if the year is negative."""
        
        for year in [-1, -342425, '-143']:
            with self.assertRaises(InvalidYearError):
                validator.validate_year(year)

    def test_validate_year_str(self):
        """Test that validate_year raises an InvalidYearError if the year is a string."""
        with self.assertRaises(InvalidYearError):
            validator.validate_year('abc')