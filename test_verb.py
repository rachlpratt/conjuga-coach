import unittest
from verb import Verb


class TestVerbCreation(unittest.TestCase):
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


class TestVerbProperties(unittest.TestCase):
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


class TestVerbConjugation(unittest.TestCase):
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
        regular -ar verb in the present tense for the pronoun yo."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("present", "yo"), "hablo")

    def test_conjugate_present2(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the present tense for the pronoun nosotros."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("present", "nosotros"), "hablamos")

    def test_conjugate_present3(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the present tense for the pronoun tú."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("present", "tú"), "bebes")

    def test_conjugate_present4(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the present tense for the pronoun vosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("present", "vosotros"), "bebéis")

    def test_conjugate_present5(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the present tense for the pronoun él/ella/Ud."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("present", "él/ella/Ud."), "vive")

    def test_conjugate_present6(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the present tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("present", "ellos/ellas/Uds."),
                         "viven")

    def test_conjugate_present7(self):
        """Verifies that the conjugate method correctly conjugates aa
        irregular verb in the present tense for the pronoun yo."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("present", "yo"), "soy")

    def test_conjugate_present8(self):
        """Verifies that the conjugate method correctly conjugates aa
        irregular verb in the present tense for the pronoun nosotros."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("present", "nosotros"), "vamos")

    def test_conjugate_preterite1(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the preterite tense for the pronoun yo."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("preterite", "yo"), "hablé")

    def test_conjugate_preterite2(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the preterite tense for the pronoun tú."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("preterite", "tú"), "hablaste")

    def test_conjugate_preterite3(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun él/ella/Ud."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("preterite", "él/ella/Ud."), "bebió")

    def test_conjugate_preterite4(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun nosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("preterite", "nosotros"), "bebimos")

    def test_conjugate_preterite5(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun vosotros."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("preterite", "vosotros"), "vivisteis")

    def test_conjugate_preterite6(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("preterite", "ellos/ellas/Uds."),
                         "vivieron")

    def test_conjugate_preterite7(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun yo."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("preterite", "yo"), "fui")

    def test_conjugate_preterite8(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun tú."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("preterite", "tú"), "fuiste")

    def test_conjugate_imperfect1(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect tense for the pronoun yo."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("imperfect", "yo"), "hablaba")

    def test_conjugate_imperfect2(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect tense for the pronoun tú."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("imperfect", "tú"), "hablabas")

    def test_conjugate_imperfect3(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun él/ella/Ud."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("imperfect", "él/ella/Ud."), "bebía")

    def test_conjugate_imperfect4(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun nosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("imperfect", "nosotros"), "bebíamos")

    def test_conjugate_imperfect5(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun vosotros."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("imperfect", "vosotros"), "vivíais")

    def test_conjugate_imperfect6(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("imperfect", "ellos/ellas/Uds."),
                         "vivían")

    def test_conjugate_imperfect7(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun yo."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("imperfect", "yo"), "iba")

    def test_conjugate_imperfect8(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun tú."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("imperfect", "tú"), "eras")

    def test_conjugate_conditional1(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the conditional tense for the pronoun yo."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("conditional", "yo"), "hablaría")

    def test_conjugate_conditional2(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the conditional tense for the pronoun tú."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("conditional", "tú"), "hablarías")

    def test_conjugate_conditional3(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the conditional tense for the pronoun
        él/ella/Ud."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("conditional", "él/ella/Ud."),
                         "bebería")

    def test_conjugate_conditional4(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the conditional tense for the pronoun nosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("conditional", "nosotros"),
                         "beberíamos")

    def test_conjugate_conditional5(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the conditional tense for the pronoun vosotros."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("conditional", "vosotros"),
                         "viviríais")

    def test_conjugate_conditional6(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the conditional tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("conditional", "ellos/ellas/Uds."),
                         "vivirían")

    def test_conjugate_conditional7(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the conditional tense for the pronoun yo."""
        verb = Verb("hacer")
        self.assertEqual(verb.conjugate("conditional", "yo"), "haría")

    def test_conjugate_conditional8(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the conditional tense for the pronoun tú."""
        verb = Verb("decir")
        self.assertEqual(verb.conjugate("conditional", "tú"), "dirías")

    def test_conjugate_future1(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the future tense for the pronoun yo."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("future", "yo"), "hablaré")

    def test_conjugate_future2(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the future tense for the pronoun tú."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("future", "tú"), "hablarás")

    def test_conjugate_future3(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the future tense for the pronoun
        él/ella/Ud."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("future", "él/ella/Ud."),
                         "beberá")

    def test_conjugate_future4(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the future tense for the pronoun nosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("future", "nosotros"),
                         "beberemos")

    def test_conjugate_future5(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the future tense for the pronoun vosotros."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("future", "vosotros"),
                         "viviréis")

    def test_conjugate_future6(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the future tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("future", "ellos/ellas/Uds."),
                         "vivirán")

    def test_conjugate_future7(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the future tense for the pronoun yo."""
        verb = Verb("hacer")
        self.assertEqual(verb.conjugate("future", "yo"), "haré")

    def test_conjugate_future8(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the future tense for the pronoun tú."""
        verb = Verb("decir")
        self.assertEqual(verb.conjugate("future", "tú"), "dirás")


if __name__ == "__main__":
    unittest.main()
