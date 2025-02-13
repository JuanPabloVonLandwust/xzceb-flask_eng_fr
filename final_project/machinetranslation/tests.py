"""Module for testing translator module"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Class to test translator functions"""
    def test_english_to_french(self):
        """Method for testing english_to_french function"""
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertNotEqual(english_to_french("hello"), "hello")

    def test_french_to_english(self):
        """Method for testing french_to_english function"""
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("bonjour"), "hello")
        self.assertNotEqual(french_to_english("bonjour"), "bonjour")

unittest.main()
