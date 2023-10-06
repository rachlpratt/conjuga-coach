import unittest
from verb import Verb


class TestVerb(unittest.TestCase):
    def test_verb_instance_type(self):
        verb = Verb("hacer")
        self.assertIsInstance(verb, Verb)

    def test_verb_infinitive1(self):
        verb = Verb("hablar")
        self.assertEqual(verb.infinitive, "hablar")

    def test_verb_infinitive2(self):
        verb = Verb("hacer")
        self.assertEqual(verb.infinitive, "hacer")

    def test_verb_infinitive3(self):
        verb = Verb("decir")
        self.assertEqual(verb.infinitive, "decir")

    def test_verb_stem1(self):
        verb = Verb("hablar")
        self.assertEqual(verb.stem, "habl")

    def test_verb_stem2(self):
        verb = Verb("hacer")
        self.assertEqual(verb.stem, "hac")

    def test_verb_stem3(self):
        verb = Verb("decir")
        self.assertEqual(verb.stem, "dec")

    def test_verb_ending1(self):
        verb = Verb("hablar")
        self.assertEqual(verb.ending, "ar")

    def test_verb_ending2(self):
        verb = Verb("hacer")
        self.assertEqual(verb.ending, "er")

    def test_verb_ending3(self):
        verb = Verb("decir")
        self.assertEqual(verb.ending, "ir")

    def test_is_regular1(self):
        verb = Verb("hablar")
        self.assertTrue(verb.is_regular)

    def test_is_regular2(self):
        verb = Verb("ser")
        self.assertFalse(verb.is_regular)


if __name__ == "__main__":
    unittest.main()
