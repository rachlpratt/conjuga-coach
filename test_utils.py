import unittest
import utils
from verb import Verb


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

    def test_get_present_participle1(self):
        """Verifies that get_present_participle returns the correct present
        participle given a regular -ar verb"""
        verb = Verb("hablar")
        self.assertEqual(utils.get_present_participle(verb), "hablando")

    def test_get_present_participle2(self):
        """Verifies that get_present_participle returns the correct present
        participle given a regular -er verb"""
        verb = Verb("beber")
        self.assertEqual(utils.get_present_participle(verb), "bebiendo")

    def test_get_present_participle3(self):
        """Verifies that get_present_participle returns the correct present
        participle given a regular -ir verb"""
        verb = Verb("vivir")
        self.assertEqual(utils.get_present_participle(verb), "viviendo")

    def test_get_present_participle4(self):
        """Verifies that get_present_participle returns the correct present
        participle given an irregular verb"""
        verb = Verb("ir")
        self.assertEqual(utils.get_present_participle(verb), "yendo")

    def test_get_past_participle1(self):
        """Verifies that get_past_participle returns the correct past
        participle given a regular -ar verb"""
        verb = Verb("hablar")
        self.assertEqual(utils.get_past_participle(verb), "hablado")

    def test_get_past_participle2(self):
        """Verifies that get_past_participle returns the correct past
        participle given a regular -er verb"""
        verb = Verb("beber")
        self.assertEqual(utils.get_past_participle(verb), "bebido")

    def test_get_past_participle3(self):
        """Verifies that get_past_participle returns the correct past
        participle given a regular -ir verb"""
        verb = Verb("vivir")
        self.assertEqual(utils.get_past_participle(verb), "vivido")

    def test_get_past_participle4(self):
        """Verifies that get_past_participle returns the correct past
        participle given an irregular verb"""
        verb = Verb("decir")
        self.assertEqual(utils.get_past_participle(verb), "dicho")
