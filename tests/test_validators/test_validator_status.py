import unittest

from app.utils.enums import BookStatus
from app.utils.validator import validator
from app.utils.exceptions import InvalidStatusError

class TestValidatorsStatus(unittest.TestCase):
    def test_validate_status_valid(self):
        """Test that validate_status returns the status if it is valid."""

        for status in [s.value for s in BookStatus]:
            with self.subTest(status=status):
                self.assertEqual(validator.validate_status(status), status)
    
    def test_validate_status_invalid(self):
        """Test that validate_status raises an InvalidStatusError if the status is invalid."""
        
        for status in ['', 'dffs', 2, None]:
            with self.assertRaises(InvalidStatusError):
                validator.validate_status(status)