import unittest
import json
from unittest.mock import patch
from dictionary import translate # Assuming dictionary.py is in the same directory or accessible via PYTHONPATH

class TestTranslateFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a dummy data.json for testing, consistent with previous steps
        dummy_data = {"apple": ["A fruit"], "banana": ["An edible fruit"], "aple": ["A typo for apple?"]}
        with open("data.json", "w") as f:
            json.dump(dummy_data, f)

    def test_word_exists(self):
        self.assertEqual(translate("apple"), ["A fruit"])
        self.assertEqual(translate("APPLE"), ["A fruit"]) # Test case insensitivity

    def test_word_not_exists(self):
        self.assertEqual(translate("orange"), "The word does not exist.Please double check it")

    @patch('builtins.input', return_value='Y')
    def test_similar_word_suggestion_yes(self, mock_input):
        # "aple" is in our dummy data, "apple" should be suggested.
        # The original data.json might have different close matches.
        # For this test, we rely on "aple" being close to "apple" and "apple" being in data.
        # Let's adjust dummy data to ensure "appel" suggests "apple"
        # No, the current dictionary.py suggests the *first* close match.
        # `get_close_matches("appel", ["apple", "aple", "banana"])` might return `['apple', 'aple']`
        # So it would suggest "apple".
        self.assertEqual(translate("appel"), ["A fruit"]) # User inputs 'Y' to "apple"

    @patch('builtins.input', return_value='N')
    def test_similar_word_suggestion_no(self, mock_input):
        self.assertEqual(translate("appel"), "The word does not exist.Please double check it") # User inputs 'N'

    @patch('builtins.input', return_value='Maybe')
    def test_similar_word_suggestion_invalid_input(self, mock_input):
        self.assertEqual(translate("appel"), "Sorry we didn't understand your entry") # User inputs something other than Y/N

    # Test for a word that is very different and has no close matches
    def test_word_far_no_suggestion(self):
        self.assertEqual(translate("xyzxyz"), "The word does not exist.Please double check it")

    # Test with an empty string
    def test_empty_string_input(self):
        self.assertEqual(translate(""), "The word does not exist.Please double check it")

if __name__ == '__main__':
    unittest.main()
