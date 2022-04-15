import unittest

from translator import english_to_french, french_to_english

class TestTranslatorModule(unittest.TestCase):
    def test_french_to_english(self):
        with self.assertRaises(ValueError):
            french_to_english(None)

        self.assertEqual(french_to_english("Bonjour"), "Hello")


    def test_english_to_french(self):
        with self.assertRaises(ValueError):
            english_to_french(None)

        self.assertEqual(english_to_french("Hello"), "Bonjour")


unittest.main()
