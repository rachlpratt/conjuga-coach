import unittest
from verb import Verb


class TestVerb(unittest.TestCase):
    def test_verb_instance_type(self):
        """Verifies that newly created verb has object type Verb."""
        verb = Verb("hacer")
        self.assertIsInstance(verb, Verb)

    def test_is_valid1(self):
        """Verifies that creating a Verb object with a valid irregular verb
        string does not raise a ValueError."""
        valid_verb = "ser"
        try:
            Verb(valid_verb)
        except ValueError:
            self.fail("Expected no ValueError")

    def test_is_valid2(self):
        """Verifies that creating a Verb object with a valid regular verb
        string does not raise a ValueError."""
        valid_verb = "hablar"
        try:
            Verb(valid_verb)
        except ValueError:
            self.fail("Expected no ValueError")

    def test_is_valid3(self):
        """Verifies that creating a Verb object with an invalid verb string
        raises a ValueError."""
        invalid_verb = "abcd"
        with self.assertRaises(ValueError):
            Verb(invalid_verb)

    def test_is_valid4(self):
        """Verifies that creating a Verb object with an empty verb string
        raises a ValueError."""
        invalid_verb = ""
        with self.assertRaises(ValueError):
            Verb(invalid_verb)

    def test_verb_infinitive1(self):
        """Verifies that the infinitive property returns the correct value
        for a Verb object."""
        verb = Verb("hablar")
        self.assertEqual(verb.infinitive, "hablar")

    def test_verb_infinitive2(self):
        """Verifies that the infinitive property returns the correct value
        for a Verb object."""
        verb = Verb("hacer")
        self.assertEqual(verb.infinitive, "hacer")

    def test_verb_infinitive3(self):
        """Verifies that the infinitive property returns the correct value
        for a Verb object."""
        verb = Verb("decir")
        self.assertEqual(verb.infinitive, "decir")

    def test_verb_stem1(self):
        """Verifies that the stem property returns the correct value
        for a Verb object."""
        verb = Verb("hablar")
        self.assertEqual(verb.stem, "habl")

    def test_verb_stem2(self):
        """Verifies that the stem property returns the correct value
        for a Verb object."""
        verb = Verb("hacer")
        self.assertEqual(verb.stem, "hac")

    def test_verb_stem3(self):
        """Verifies that the stem property returns the correct value
        for a Verb object."""
        verb = Verb("decir")
        self.assertEqual(verb.stem, "dec")

    def test_verb_ending1(self):
        """Verifies that the ending property returns the correct value
        for a Verb object."""
        verb = Verb("hablar")
        self.assertEqual(verb.ending, "ar")

    def test_verb_ending2(self):
        """Verifies that the ending property returns the correct value
        for a Verb object."""
        verb = Verb("hacer")
        self.assertEqual(verb.ending, "er")

    def test_verb_ending3(self):
        """Verifies that the ending property returns the correct value
        for a Verb object."""
        verb = Verb("decir")
        self.assertEqual(verb.ending, "ir")

    def test_is_regular1(self):
        """Verifies that the is_regular property returns True for a
        regular verb."""
        verb = Verb("hablar")
        self.assertTrue(verb.is_regular)

    def test_is_regular2(self):
        """Verifies that the is_regular property returns False for an
        irregular verb."""
        verb = Verb("ser")
        self.assertFalse(verb.is_regular)

    def test_str_method(self):
        """Verifies that the __str__ method returns the expected string
        representation for a Verb object."""
        verb = Verb("hacer")
        self.assertEqual(str(verb), "Verb: hacer")

    def test_str_method2(self):
        """Verifies that the __str__ method returns the expected string
        representation for a Verb object."""
        verb = Verb("decir")
        self.assertEqual(str(verb), "Verb: decir")

    def test_conjugate1(self):
        """Verifies that a ValueError is raised when an invalid tense is passed
        to the conjugate method."""
        verb = Verb("hablar")
        with self.assertRaises(ValueError):
            verb.conjugate("abcd", "yo")

    def test_conjugate2(self):
        """Verifies that a ValueError is raised when an empty tense is passed
        to the conjugate method."""
        verb = Verb("hablar")
        with self.assertRaises(ValueError):
            verb.conjugate("", "yo")

    def test_conjugate3(self):
        """Verifies that a ValueError is raised when an invalid pronoun is
        passed to the conjugate method."""
        verb = Verb("hablar")
        with self.assertRaises(ValueError):
            verb.conjugate("present", "abcd")

    def test_conjugate4(self):
        """Verifies that a ValueError is raised when an empty pronoun is passed
        to the conjugate method."""
        verb = Verb("hablar")
        with self.assertRaises(ValueError):
            verb.conjugate("present", "")

    def test_conjugate5(self):
        """Verifies that a ValueError is raised when an invalid tense and an
        invalid pronoun are passed to the conjugate method."""
        verb = Verb("hablar")
        with self.assertRaises(ValueError):
            verb.conjugate("abcd", "abcd")

    def test_conjugate6(self):
        """Verifies that a ValueError is raised when an empty tense and an
        empty pronoun are passed to the conjugate method."""
        verb = Verb("hablar")
        with self.assertRaises(ValueError):
            verb.conjugate("", "")

    def test_conjugate7(self):
        """Verifies that a ValueError is raised when a non-string tense and
        pronoun are passed to the conjugate method."""
        verb = Verb("hablar")
        with self.assertRaises(ValueError):
            verb.conjugate(1, 1)

    def test_conjugate_present1(self):
        """Verifies that the conjugate method correctly conjugates a
        regular verb in the present tense for a specified pronoun."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("present", "yo"), "hablo")

    def test_conjugate_present2(self):
        """Verifies that the conjugate method correctly conjugates a
        regular verb in the present tense for a specified pronoun."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("present", "nosotros"), "bebemos")

    def test_conjugate_present3(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the present tense for a specified pronoun."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("present", "yo"), "soy")

    def test_conjugate_present4(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the present tense for a specified pronoun."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("present", "nosotros"), "vamos")


if __name__ == "__main__":
    unittest.main()
