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
        regular -ar verb in the preterite tense for the pronoun él/ella/Ud."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("preterite", "él/ella/Ud."), "habló")

    def test_conjugate_preterite4(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the preterite tense for the pronoun nosotros."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("preterite", "nosotros"), "hablamos")

    def test_conjugate_preterite5(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the preterite tense for the pronoun vosotros."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("preterite", "vosotros"), "hablasteis")

    def test_conjugate_preterite6(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the preterite tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("preterite", "ellos/ellas/Uds."),
                         "hablaron")

    def test_conjugate_preterite7(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun yo."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("preterite", "yo"), "bebí")

    def test_conjugate_preterite8(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun tú."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("preterite", "tú"), "bebiste")

    def test_conjugate_preterite9(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun él/ella/Ud."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("preterite", "él/ella/Ud."), "bebió")

    def test_conjugate_preterite10(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun nosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("preterite", "nosotros"), "bebimos")

    def test_conjugate_preterite11(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun vosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("preterite", "vosotros"), "bebisteis")

    def test_conjugate_preterite12(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("preterite", "ellos/ellas/Uds."),
                         "bebieron")

    def test_conjugate_preterite13(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun yo."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("preterite", "yo"), "viví")

    def test_conjugate_preterite14(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun tú."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("preterite", "tú"), "viviste")

    def test_conjugate_preterite15(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun él/ella/Ud."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("preterite", "él/ella/Ud."), "vivió")

    def test_conjugate_preterite16(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun nosotros."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("preterite", "nosotros"), "vivimos")

    def test_conjugate_preterite17(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun vosotros."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("preterite", "vosotros"), "vivisteis")

    def test_conjugate_preterite18(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("preterite", "ellos/ellas/Uds."),
                         "vivieron")

    def test_conjugate_preterite19(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun yo."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("preterite", "yo"), "fui")

    def test_conjugate_preterite20(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun tú."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("preterite", "tú"), "fuiste")

    def test_conjugate_preterite21(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun él/ella/Ud."""
        verb = Verb("decir")
        self.assertEqual(verb.conjugate("preterite", "él/ella/Ud."), "dijo")

    def test_conjugate_preterite22(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun nosotros."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("preterite", "nosotros"), "fuimos")

    def test_conjugate_preterite23(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun vosotros."""
        verb = Verb("hacer")
        self.assertEqual(verb.conjugate("preterite", "vosotros"), "hicisteis")

    def test_conjugate_preterite24(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("preterite", "ellos/ellas/Uds."),
                         "fueron")

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
        regular -ar verb in the imperfect tense for the pronoun él/ella/Ud."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("imperfect", "él/ella/Ud."), "hablaba")

    def test_conjugate_imperfect4(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect tense for the pronoun nosotros."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("imperfect", "nosotros"), "hablábamos")

    def test_conjugate_imperfect5(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect tense for the pronoun vosotros."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("imperfect", "vosotros"), "hablabais")

    def test_conjugate_imperfect6(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("hablar")
        self.assertEqual(verb.conjugate("imperfect", "ellos/ellas/Uds."),
                         "hablaban")

    def test_conjugate_imperfect7(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun yo."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("imperfect", "yo"), "bebía")

    def test_conjugate_imperfect8(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun tú."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("imperfect", "tú"), "bebías")

    def test_conjugate_imperfect9(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun él/ella/Ud."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("imperfect", "él/ella/Ud."), "bebía")

    def test_conjugate_imperfect10(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun nosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("imperfect", "nosotros"), "bebíamos")

    def test_conjugate_imperfect11(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun vosotros."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("imperfect", "vosotros"), "bebíais")

    def test_conjugate_imperfect12(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("beber")
        self.assertEqual(verb.conjugate("imperfect", "ellos/ellas/Uds."),
                         "bebían")

    def test_conjugate_imperfect13(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun yo."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("imperfect", "yo"), "vivía")

    def test_conjugate_imperfect14(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun tú."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("imperfect", "tú"), "vivías")

    def test_conjugate_imperfect15(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun él/ella/Ud."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("imperfect", "él/ella/Ud."), "vivía")

    def test_conjugate_imperfect16(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun nosotros."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("imperfect", "nosotros"), "vivíamos")

    def test_conjugate_imperfect17(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun vosotros."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("imperfect", "vosotros"), "vivíais")

    def test_conjugate_imperfect18(self):
        """Verifies that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("vivir")
        self.assertEqual(verb.conjugate("imperfect", "ellos/ellas/Uds."),
                         "vivían")

    def test_conjugate_imperfect19(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun yo."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("imperfect", "yo"), "iba")

    def test_conjugate_imperfect20(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun tú."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("imperfect", "tú"), "eras")

    def test_conjugate_imperfect21(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun él/ella/Ud."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("imperfect", "él/ella/Ud."), "era")

    def test_conjugate_imperfect22(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun nosotros."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("imperfect", "nosotros"), "íbamos")

    def test_conjugate_imperfect23(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun vosotros."""
        verb = Verb("ser")
        self.assertEqual(verb.conjugate("imperfect", "vosotros"), "erais")

    def test_conjugate_imperfect24(self):
        """Verifies that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun
        ellos/ellas/Uds."""
        verb = Verb("ir")
        self.assertEqual(verb.conjugate("imperfect", "ellos/ellas/Uds."),
                         "iban")


if __name__ == "__main__":
    unittest.main()
