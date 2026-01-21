"""
Unit tests for utility functions.
These tests can be used to validate merge results.
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import format_result


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_format_result(self):
        """Test result formatting."""
        self.assertEqual(format_result(3.14159, 2), "3.14")
        self.assertEqual(format_result(10, 0), "10")
        self.assertEqual(format_result(2.5, 1), "2.5")
        self.assertEqual(format_result(100.999, 2), "101.00")


if __name__ == '__main__':
    unittest.main()
