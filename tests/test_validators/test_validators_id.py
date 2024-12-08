import unittest

from app.utils.validator import validator
from app.utils.exceptions import InvalidIDError

class TestValidatorsID(unittest.TestCase):
    def test_validate_id_positive(self):
        """Test the validate_id function with positive numbers."""

        for number in [1, 5, 342425]:
            with self.subTest(number=number):
                self.assertEqual(validator.validate_id(number), number)
    

    def test_validate_id_negative(self):
        """Test the validate_id function with negative numbers."""

        for number in [-1, -5, -342425]:
            with self.subTest(number=number):
                with self.assertRaises(InvalidIDError):
                    validator.validate_id(number)
    

    def test_validate_id_zero(self):
        """Test the validate_id function with zero."""

        with self.assertRaises(InvalidIDError):
            validator.validate_id(0)


    def test_validate_id_string(self):
        """Test the validate_id function with strings."""
        
        with self.assertRaises(InvalidIDError):
            validator.validate_id('string')