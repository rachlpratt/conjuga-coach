import unittest
from verb import Verb


class TestVerb(unittest.TestCase):
    def test_verb_instance_type(self):
        verb = Verb("hacer")
        self.assertIsInstance(verb, Verb)

    def test_is_valid_verb1(self):
        valid_verb = "ser"
        try:
            Verb(valid_verb)
        except ValueError:
            self.fail("Expected no ValueError")

    def test_is_valid_verb2(self):
        valid_verb = "hablar"
        try:
            Verb(valid_verb)
        except ValueError:
            self.fail("Expected no ValueError")

    def test_is_valid_verb3(self):
        invalid_verb = "abcd"
        with self.assertRaises(ValueError):
            Verb(invalid_verb)

    def test_is_valid_verb4(self):
        invalid_verb = ""
        with self.assertRaises(ValueError):
            Verb(invalid_verb)

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

    def test_str_method(self):
        verb = Verb("hacer")
        self.assertEqual(str(verb), "Verb: hacer")

    def test_str_method2(self):
        verb = Verb("decir")
        self.assertEqual(str(verb), "Verb: decir")


if __name__ == "__main__":
    unittest.main()
