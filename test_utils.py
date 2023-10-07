import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_is_valid_tense1(self):
        """Verifies that is_valid_tense returns True given a valid tense."""
        self.assertTrue(utils.is_valid_tense("present"))

    def test_is_valid_tense2(self):
        """Verifies that is_valid_tense returns False given
        an invalid tense."""
        self.assertTrue(utils.is_valid_tense("present"))
        self.assertFalse(utils.is_valid_tense("abcd"))

    def test_is_valid_tense3(self):
        """Verifies that is_valid_tense returns False given
        an invalid, non-string tense."""
        self.assertFalse(utils.is_valid_tense(1))

    def test_is_valid_tense4(self):
        """Verifies that is_valid_tense returns False given
        an invalid, empty string tense."""
        self.assertFalse(utils.is_valid_tense(""))

    def test_is_valid_pronoun1(self):
        """Verifies that is_valid_pronoun returns True given
        a valid pronoun."""
        self.assertTrue(utils.is_valid_pronoun("yo"))

    def test_is_valid_pronoun2(self):
        """Verifies that is_valid_pronoun returns True given
        a valid pronoun."""
        self.assertTrue(utils.is_valid_pronoun("vosotros"))

    def test_is_valid_pronoun3(self):
        """Verifies that is_valid_pronoun returns False given
        an invalid pronoun."""
        self.assertFalse(utils.is_valid_pronoun("abcd"))

    def test_is_valid_pronoun4(self):
        """Verifies that is_valid_pronoun returns False given
        an invalid, non-string pronoun."""
        self.assertFalse(utils.is_valid_pronoun(2))

    def test_is_valid_pronoun5(self):
        """Verifies that is_valid_pronoun returns False given
        an invalid, empty string pronoun."""
        self.assertFalse(utils.is_valid_pronoun(""))
