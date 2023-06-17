"""Module for testing translator module"""
import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Class to test translator functions"""
    def test_english_to_french(self):
        """Method for testing english_to_french function"""
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("Good morning"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")

    def test_french_to_english(self):
        """Method for testing french_to_english function"""
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

unittest.main()
