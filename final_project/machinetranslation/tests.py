from translator import english_to_french, french_to_english
import unittest


class translate_test(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french("Hello!"), "Bonjour !")
    
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test3(self):
        self.assertEqual(french_to_english(" "), " ")

    def test4(self):
        self.assertEqual(english_to_french(" "), " ")


if __name__ == "__main__":
    unittest.main()

        