from django.test import TestCase

from app.calc import add, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that 2 numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that 2 numbers are subtracted """
        self.assertEqual(sub(9, 3),6)