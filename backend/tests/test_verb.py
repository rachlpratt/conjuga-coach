import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from backend.app.extensions import db
from backend.app.resources.verb import Verb
from backend.tests.setup_tests import setup_testing_db


class TestVerbs(unittest.TestCase):
    app: Flask
    db: SQLAlchemy

    @classmethod
    def setUpClass(cls):
        """Set up testing database."""
        setup_testing_db(cls)

    @classmethod
    def tearDownClass(cls):
        """Tear down testing database."""
        with cls.app.app_context():
            db.drop_all()

    def test_verb_instance_type(self):
        """Verify that newly created verb has object type Verb."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertIsInstance(verb, Verb)

    def test_verb_creation1(self):
        """Verify that creating a Verb object with a valid irregular verb
        string does not raise a ValueError."""
        with self.app.app_context():
            valid_verb = "ser"
            try:
                Verb(valid_verb)
            except ValueError:
                self.fail("Expected no ValueError")

    def test_verb_creation2(self):
        """Verify that creating a Verb object with a valid regular verb
        string does not raise a ValueError."""
        with self.app.app_context():
            valid_verb = "hablar"
            try:
                Verb(valid_verb)
            except ValueError:
                self.fail("Expected no ValueError")

    def test_verb_creation3(self):
        """Verify that creating a Verb object with a valid regular uppercase
        verb string does not raise a ValueError."""
        with self.app.app_context():
            valid_verb = "HABLAR"
            try:
                Verb(valid_verb)
            except ValueError:
                self.fail("Expected no ValueError")

    def test_verb_creation4(self):
        """Verify that creating a Verb object with an invalid verb string
        raises a ValueError."""
        with self.app.app_context():
            invalid_verb = "abcd"
            with self.assertRaises(ValueError):
                Verb(invalid_verb)

    def test_verb_creation5(self):
        """Verify that creating a Verb object with an empty verb string
        raises a ValueError."""
        with self.app.app_context():
            invalid_verb = ""
            with self.assertRaises(ValueError):
                Verb(invalid_verb)

    def test_verb_infinitive1(self):
        """Verify that the infinitive property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.infinitive, "hablar")

    def test_verb_infinitive2(self):
        """Verify that the infinitive property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.infinitive, "hacer")

    def test_verb_infinitive3(self):
        """Verify that the infinitive property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.infinitive, "decir")

    def test_verb_stem1(self):
        """Verify that the stem property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.stem, "habl")

    def test_verb_stem2(self):
        """Verify that the stem property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.stem, "hac")

    def test_verb_stem3(self):
        """Verify that the stem property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.stem, "dec")

    def test_verb_ending1(self):
        """Verify that the ending property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.ending, "ar")

    def test_verb_ending2(self):
        """Verify that the ending property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.ending, "er")

    def test_verb_ending3(self):
        """Verify that the ending property returns the correct value
        for a Verb object."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.ending, "ir")

    def test_is_regular1(self):
        """Verify that the is_regular property returns True for a regular
        verb."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertTrue(verb.is_regular)

    def test_is_regular2(self):
        """Verify that the is_regular property returns False for an
        irregular verb."""
        with self.app.app_context():
            verb = Verb("ser")
            self.assertFalse(verb.is_regular)

    def test_str_method(self):
        """Verify that the __str__ method returns the expected string
        representation for a Verb object."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(str(verb), "Verb: hacer")

    def test_str_method2(self):
        """Verify that the __str__ method returns the expected string
        representation for a Verb object."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(str(verb), "Verb: decir")

    def test_conjugate1(self):
        """Verify that a ValueError is raised when an invalid tense is passed
        to the conjugate method."""
        with self.app.app_context():
            verb = Verb("hablar")
            with self.assertRaises(ValueError):
                verb.conjugate("abcd", "yo")

    def test_conjugate2(self):
        """Verify that a ValueError is raised when an empty tense is passed
        to the conjugate method."""
        with self.app.app_context():
            verb = Verb("hablar")
            with self.assertRaises(ValueError):
                verb.conjugate("", "yo")

    def test_conjugate3(self):
        """Verify that a ValueError is raised when an invalid pronoun is
        passed to the conjugate method."""
        with self.app.app_context():
            verb = Verb("hablar")
            with self.assertRaises(ValueError):
                verb.conjugate("present", "abcd")

    def test_conjugate4(self):
        """Verify that a ValueError is raised when an empty pronoun is passed
        to the conjugate method."""
        with self.app.app_context():
            verb = Verb("hablar")
            with self.assertRaises(ValueError):
                verb.conjugate("present", "")

    def test_conjugate5(self):
        """Verify that a ValueError is raised when an invalid tense and an
        invalid pronoun are passed to the conjugate method."""
        with self.app.app_context():
            verb = Verb("hablar")
            with self.assertRaises(ValueError):
                verb.conjugate("abcd", "abcd")

    def test_conjugate6(self):
        """Verify that a ValueError is raised when an empty tense and an
        empty pronoun are passed to the conjugate method."""
        with self.app.app_context():
            verb = Verb("hablar")
            with self.assertRaises(ValueError):
                verb.conjugate("", "")

    def test_conjugate7(self):
        """Verify that a ValueError is raised when a non-string tense and
        pronoun are passed to the conjugate method."""
        with self.app.app_context():
            verb = Verb("hablar")
            with self.assertRaises(ValueError):
                verb.conjugate(1, 1)

    def test_conjugate_present1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the present tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present", "yo"), "hablo")

    def test_conjugate_present2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the present tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present", "nosotros"), "hablamos")

    def test_conjugate_present3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the present tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present", "tú"), "bebes")

    def test_conjugate_present4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the present tense for the pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present", "vosotros"), "bebéis")

    def test_conjugate_present5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the present tense for the pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present", "él/ella/Ud."), "vive")

    def test_conjugate_present6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the present tense for the pronoun
        ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present", "ellos/ellas/Uds."),
                             "viven")

    def test_conjugate_present7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("ser")
            self.assertEqual(verb.conjugate("present", "yo"), "soy")

    def test_conjugate_present8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("ir")
            self.assertEqual(verb.conjugate("present", "nosotros"), "vamos")

    def test_conjugate_preterite1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the preterite tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("preterite", "yo"), "hablé")

    def test_conjugate_preterite2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the preterite tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("preterite", "tú"), "hablaste")

    def test_conjugate_preterite3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("preterite", "él/ella/Ud."), 
                             "bebió")

    def test_conjugate_preterite4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the preterite tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("preterite", "nosotros"), 
                             "bebimos")

    def test_conjugate_preterite5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("preterite", "vosotros"), 
                             "vivisteis")

    def test_conjugate_preterite6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the preterite tense for the pronoun
        ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("preterite", "ellos/ellas/Uds."),
                             "vivieron")

    def test_conjugate_preterite7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("ir")
            self.assertEqual(verb.conjugate("preterite", "yo"), "fui")

    def test_conjugate_preterite8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the preterite tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("ser")
            self.assertEqual(verb.conjugate("preterite", "tú"), "fuiste")

    def test_conjugate_imperfect1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("imperfect", "yo"), "hablaba")

    def test_conjugate_imperfect2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("imperfect", "tú"), "hablabas")

    def test_conjugate_imperfect3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("imperfect", "él/ella/Ud."), 
                             "bebía")

    def test_conjugate_imperfect4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the imperfect tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("imperfect", "nosotros"), 
                             "bebíamos")

    def test_conjugate_imperfect5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("imperfect", "vosotros"), 
                             "vivíais")

    def test_conjugate_imperfect6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect tense for the pronoun
        ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("imperfect", "ellos/ellas/Uds."),
                             "vivían")

    def test_conjugate_imperfect7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("ir")
            self.assertEqual(verb.conjugate("imperfect", "yo"), "iba")

    def test_conjugate_imperfect8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the imperfect tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("ser")
            self.assertEqual(verb.conjugate("imperfect", "tú"), "eras")

    def test_conjugate_conditional1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the conditional tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("conditional", "yo"), "hablaría")

    def test_conjugate_conditional2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the conditional tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("conditional", "tú"), "hablarías")

    def test_conjugate_conditional3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the conditional tense for the pronoun
        él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("conditional", "él/ella/Ud."),
                             "bebería")

    def test_conjugate_conditional4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the conditional tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("conditional", "nosotros"),
                             "beberíamos")

    def test_conjugate_conditional5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the conditional tense for the pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("conditional", "vosotros"),
                             "viviríais")

    def test_conjugate_conditional6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the conditional tense for the pronoun
        ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("conditional", "ellos/ellas/Uds."),
                             "vivirían")

    def test_conjugate_conditional7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the conditional tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("conditional", "yo"), "haría")

    def test_conjugate_conditional8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the conditional tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("conditional", "tú"), "dirías")

    def test_conjugate_future1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the future tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("future", "yo"), "hablaré")

    def test_conjugate_future2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the future tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("future", "tú"), "hablarás")

    def test_conjugate_future3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the future tense for the pronoun
        él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("future", "él/ella/Ud."),
                             "beberá")

    def test_conjugate_future4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the future tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("future", "nosotros"),
                             "beberemos")

    def test_conjugate_future5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the future tense for the pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("future", "vosotros"),
                             "viviréis")

    def test_conjugate_future6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the future tense for the pronoun
        ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("future", "ellos/ellas/Uds."),
                             "vivirán")

    def test_conjugate_future7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the future tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("future", "yo"), "haré")

    def test_conjugate_future8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the future tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("future", "tú"), "dirás")

    def test_conjugate_present_subjunctive1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the present subjunctive tense for the pronoun
        yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present_subjunctive", "yo"), 
                             "hable")

    def test_conjugate_present_subjunctive2(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the present subjunctive tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present_subjunctive", "tú"), 
                             "hables")

    def test_conjugate_present_subjunctive3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the present subjunctive tense for the pronoun
        él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present_subjunctive", 
                                            "él/ella/Ud."), "beba")

    def test_conjugate_present_subjunctive4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the present subjunctive tense for the pronoun
        nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present_subjunctive", "nosotros"),
                             "bebamos")

    def test_conjugate_present_subjunctive5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the present subjunctive tense for the pronoun
        vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present_subjunctive", "vosotros"),
                             "viváis")

    def test_conjugate_present_subjunctive6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the present subjunctive tense for the pronoun
        ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present_subjunctive",
                                            "ellos/ellas/Uds."),
                             "vivan")

    def test_conjugate_present_subjunctive7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present subjunctive tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("present_subjunctive", "yo"), 
                             "haga")

    def test_conjugate_present_subjunctive8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present subjunctive tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("present_subjunctive", "tú"), 
                             "digas")

    def test_conjugate_imperfect_subjunctive_ra1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect subjunctive (-ra) tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_ra", "yo"),
                             "hablara")

    def test_conjugate_imperfect_subjunctive_ra2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect subjunctive (-ra) tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_ra", "tú"),
                             "hablaras")

    def test_conjugate_imperfect_subjunctive_ra3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the imperfect subjunctive (-ra) tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_ra",
                                            "él/ella/Ud."), "bebiera")

    def test_conjugate_imperfect_subjunctive_ra4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the imperfect subjunctive (-ra) tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_ra", 
                                            "nosotros"), "bebiéramos")

    def test_conjugate_imperfect_subjunctive_ra5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect subjunctive (-ra) tense for the
        pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_ra", 
                                            "vosotros"), "vivierais")

    def test_conjugate_imperfect_subjunctive_ra6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect subjunctive (-ra) tense for the
        pronoun ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_ra",
                                            "ellos/ellas/Uds."),
                             "vivieran")

    def test_conjugate_imperfect_subjunctive_ra7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the imperfect subjunctive (-ra) tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_ra", "yo"),
                             "hiciera")

    def test_conjugate_imperfect_subjunctive_ra8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the imperfect subjunctive (-ra) tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_ra", "tú"),
                             "dijeras")

    def test_conjugate_imperfect_subjunctive_se1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect subjunctive (-se) tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_se", "yo"),
                             "hablase")

    def test_conjugate_imperfect_subjunctive_se2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the imperfect subjunctive (-se) tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_se", "tú"),
                             "hablases")

    def test_conjugate_imperfect_subjunctive_se3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the imperfect subjunctive (-se) tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_se",
                                            "él/ella/Ud."),
                             "bebiese")

    def test_conjugate_imperfect_subjunctive_se4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the imperfect subjunctive (-se) tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_se",
                                            "nosotros"), "bebiésemos")

    def test_conjugate_imperfect_subjunctive_se5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect subjunctive (-se) tense for the
        pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_se",
                                            "vosotros"), "vivieseis")

    def test_conjugate_imperfect_subjunctive_se6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the imperfect subjunctive (-se) tense for the
        pronoun ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_se",
                                            "ellos/ellas/Uds."), "viviesen")

    def test_conjugate_imperfect_subjunctive_se7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the imperfect subjunctive (-se) tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_se", "yo"),
                             "hiciese")

    def test_conjugate_imperfect_subjunctive_se8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the imperfect subjunctive (-se) tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("imperfect_subjunctive_se", "tú"),
                             "dijeses")

    def test_conjugate_affirmative_imperative1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the affirmative imperative tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("affirmative_imperative", "tú"),
                             "habla")

    def test_conjugate_affirmative_imperative2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the affirmative imperative tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("affirmative_imperative",
                                            "nosotros"), "hablemos")

    def test_conjugate_affirmative_imperative3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the affirmative imperative tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("affirmative_imperative", "tú"),
                             "bebe")

    def test_conjugate_affirmative_imperative4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the affirmative imperative tense for the
        pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("affirmative_imperative",
                                            "vosotros"), "bebed")

    def test_conjugate_affirmative_imperative5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the affirmative imperative tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("affirmative_imperative",
                                            "él/ella/Ud."), "viva")

    def test_conjugate_affirmative_imperative6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the affirmative imperative tense for the pronoun
        ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("affirmative_imperative",
                                            "ellos/ellas/Uds."), "vivan")

    def test_conjugate_affirmative_imperative7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the affirmative imperative tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("ir")
            self.assertEqual(verb.conjugate("affirmative_imperative", "tú"),
                             "ve")

    def test_conjugate_affirmative_imperative8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the affirmative imperative tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("affirmative_imperative", 
                                            "nosotros"), "digamos")

    def test_conjugate_affirmative_imperative9(self):
        """Verify that attempting to conjugate verb in first person with
        affirmative imperative tense raises error."""
        with self.app.app_context():
            verb = Verb("ir")
            with self.assertRaises(ValueError):
                verb.conjugate("affirmative_imperative", "yo")

    def test_conjugate_negative_imperative1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the negative imperative tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("negative_imperative", "tú"),
                             "no hables")

    def test_conjugate_negative_imperative2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the negative imperative tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("negative_imperative", "nosotros"),
                             "no hablemos")

    def test_conjugate_negative_imperative3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the negative imperative tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("negative_imperative", "tú"),
                             "no bebas")

    def test_conjugate_negative_imperative4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the negative imperative tense for the
        pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("negative_imperative", "vosotros"),
                             "no bebáis")

    def test_conjugate_negative_imperative5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the negative imperative tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("negative_imperative",
                                            "él/ella/Ud."), "no viva")

    def test_conjugate_negative_imperative6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the negative imperative tense for the pronoun
        ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("negative_imperative",
                                            "ellos/ellas/Uds."), "no vivan")

    def test_conjugate_negative_imperative7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the negative imperative tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("ir")
            self.assertEqual(verb.conjugate("negative_imperative", "tú"),
                             "no vayas")

    def test_conjugate_negative_imperative8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the negative imperative tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("negative_imperative", "nosotros"),
                             "no digamos")

    def test_conjugate_negative_imperative9(self):
        """Verify that attempting to conjugate verb in first person with
        negative imperative tense raises error."""
        with self.app.app_context():
            verb = Verb("ir")
            with self.assertRaises(ValueError):
                verb.conjugate("negative_imperative", "yo")

    def test_conjugate_present_progressive1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the present progressive tense for the pronoun yo"""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present_progressive", "yo"),
                             "estoy hablando")

    def test_conjugate_present_progressive2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the present progressive tense for the pronoun tú"""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present_progressive", "tú"),
                             "estás hablando")

    def test_conjugate_present_progressive3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the present progressive tense for the
        pronoun nosotros"""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present_progressive", "nosotros"),
                             "estamos bebiendo")

    def test_conjugate_present_progressive4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the present progressive tense for the
        pronoun vosotros"""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present_progressive", "vosotros"),
                             "estáis bebiendo")

    def test_conjugate_present_progressive5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the present progressive tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present_progressive", 
                                            "él/ella/Ud."), "está viviendo")

    def test_conjugate_present_progressive6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the present progressive tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present_progressive",
                             "ellos/ellas/Uds."), "están viviendo")

    def test_conjugate_present_progressive7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present progressive tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("ir")
            self.assertEqual(verb.conjugate("present_progressive", 
                                            "él/ella/Ud."), "está yendo")

    def test_conjugate_present_progressive8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present progressive tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("present_progressive", "yo"),
                             "estoy diciendo")

    def test_conjugate_past_progressive1(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the past progressive tense for the pronoun yo"""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("past_progressive", "yo"),
                             "estaba hablando")

    def test_conjugate_past_progressive2(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ar verb in the past progressive tense for the pronoun tú"""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("past_progressive", "tú"),
                             "estabas hablando")

    def test_conjugate_past_progressive3(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the past progressive tense for the
        pronoun nosotros"""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("past_progressive", "nosotros"),
                             "estábamos bebiendo")

    def test_conjugate_past_progressive4(self):
        """Verify that the conjugate method correctly conjugates a
        regular -er verb in the past progressive tense for the
        pronoun vosotros"""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("past_progressive", "vosotros"),
                             "estabais bebiendo")

    def test_conjugate_past_progressive5(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the past progressive tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("past_progressive", "él/ella/Ud."),
                             "estaba viviendo")

    def test_conjugate_past_progressive6(self):
        """Verify that the conjugate method correctly conjugates a
        regular -ir verb in the past progressive tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("past_progressive",
                             "ellos/ellas/Uds."),"estaban viviendo")

    def test_conjugate_past_progressive7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the past progressive tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("ir")
            self.assertEqual(verb.conjugate("past_progressive", "él/ella/Ud."),
                             "estaba yendo")

    def test_conjugate_past_progressive8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the past progressive tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("past_progressive", "yo"),
                             "estaba diciendo")

    def test_conjugate_present_perfect1(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the present perfect tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present_perfect", "yo"),
                             "he hablado")

    def test_conjugate_present_perfect2(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the present perfect tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present_perfect", "tú"),
                             "has hablado")

    def test_conjugate_present_perfect3(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the present perfect tense for the pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present_perfect", "él/ella/Ud."),
                             "ha bebido")

    def test_conjugate_present_perfect4(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the present perfect tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present_perfect", "nosotros"),
                             "hemos bebido")

    def test_conjugate_present_perfect5(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the present perfect tense for the pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present_perfect", "vosotros"),
                             "habéis vivido")

    def test_conjugate_present_perfect6(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the present perfect tense for the
        pronoun ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present_perfect", 
                                            "ellos/ellas/Uds."), "han vivido")

    def test_conjugate_present_perfect7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present perfect tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("present_perfect", "yo"),
                             "he hecho")

    def test_conjugate_present_perfect8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present perfect tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("present_perfect", "tú"),
                             "has dicho")

    def test_conjugate_pluperfect1(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the pluperfect tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("pluperfect", "yo"), 
                             "había hablado")

    def test_conjugate_pluperfect2(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the pluperfect tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("pluperfect", "tú"), 
                             "habías hablado")

    def test_conjugate_pluperfect3(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the pluperfect tense for the pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("pluperfect", "él/ella/Ud."),
                             "había bebido")

    def test_conjugate_pluperfect4(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the pluperfect tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("pluperfect", "nosotros"),
                             "habíamos bebido")

    def test_conjugate_pluperfect5(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the pluperfect tense for the pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("pluperfect", "vosotros"),
                             "habíais vivido")

    def test_conjugate_pluperfect6(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the pluperfect tense for the pronoun ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("pluperfect", "ellos/ellas/Uds."),
                             "habían vivido")

    def test_conjugate_pluperfect7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the pluperfect tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("pluperfect", "yo"), "había hecho")

    def test_conjugate_pluperfect8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the pluperfect tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("pluperfect", "tú"),
                             "habías dicho")

    def test_conjugate_future_perfect1(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the future perfect tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("future_perfect", "yo"),
                             "habré hablado")

    def test_conjugate_future_perfect2(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the future perfect tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("future_perfect", "tú"),
                             "habrás hablado")

    def test_conjugate_future_perfect3(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the future perfect tense for the pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("future_perfect", "él/ella/Ud."),
                             "habrá bebido")

    def test_conjugate_future_perfect4(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the future perfect tense for the pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("future_perfect", "nosotros"),
                             "habremos bebido")

    def test_conjugate_future_perfect5(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the future perfect tense for the pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("future_perfect", "vosotros"),
                             "habréis vivido")

    def test_conjugate_future_perfect6(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the future perfect tense for the
        pronoun ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("future_perfect", 
                             "ellos/ellas/Uds."), "habrán vivido")

    def test_conjugate_future_perfect7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the future perfect tense for the pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("future_perfect", "yo"),
                             "habré hecho")

    def test_conjugate_future_perfect8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the future perfect tense for the pronoun tú."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("future_perfect", "tú"),
                             "habrás hecho")

    def test_conjugate_present_perfect_subjunctive1(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the present perfect subjunctive tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present_perfect_subjunctive", 
                                            "yo"), "haya hablado")

    def test_conjugate_present_perfect_subjunctive2(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the present perfect subjunctive tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("present_perfect_subjunctive", 
                                            "tú"), "hayas hablado")

    def test_conjugate_present_perfect_subjunctive3(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the present perfect subjunctive tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present_perfect_subjunctive",
                                            "él/ella/Ud."), "haya bebido")

    def test_conjugate_present_perfect_subjunctive4(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the present perfect subjunctive tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("present_perfect_subjunctive",
                                            "nosotros"), "hayamos bebido")

    def test_conjugate_present_perfect_subjunctive5(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the present perfect subjunctive tense for the
        pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present_perfect_subjunctive",
                                            "vosotros"), "hayáis vivido")

    def test_conjugate_present_perfect_subjunctive6(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the present perfect subjunctive tense for the
        pronoun ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("present_perfect_subjunctive",
                             "ellos/ellas/Uds."), "hayan vivido")

    def test_conjugate_present_perfect_subjunctive7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present perfect subjunctive tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("present_perfect_subjunctive", 
                                            "yo"), "haya hecho")

    def test_conjugate_present_perfect_subjunctive8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the present perfect subjunctive tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("present_perfect_subjunctive", 
                                            "tú"), "hayas hecho")

    def test_conjugate_pluperfect_subjunctive_ra1(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the pluperfect subjunctive (-ra) tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_ra", "yo"),
                             "hubiera hablado")

    def test_conjugate_pluperfect_subjunctive_ra2(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the pluperfect subjunctive (-ra) tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_ra", "tú"),
                             "hubieras hablado")

    def test_conjugate_pluperfect_subjunctive_ra3(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the pluperfect subjunctive (-ra) tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_ra",
                                            "él/ella/Ud."), "hubiera bebido")

    def test_conjugate_pluperfect_subjunctive_ra4(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the pluperfect subjunctive (-ra) tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_ra",
                                            "nosotros"), "hubiéramos bebido")

    def test_conjugate_pluperfect_subjunctive_ra5(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the pluperfect subjunctive (-ra) tense for the
        pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_ra",
                                            "vosotros"), "hubierais vivido")

    def test_conjugate_pluperfect_subjunctive_ra6(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the pluperfect subjunctive (-ra) tense for the
        pronoun ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_ra",
                             "ellos/ellas/Uds."), "hubieran vivido")

    def test_conjugate_pluperfect_subjunctive_ra7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the pluperfect subjunctive (-ra) tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_ra", "yo"),
                             "hubiera hecho")

    def test_conjugate_pluperfect_subjunctive_ra8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the pluperfect subjunctive (-ra) tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_ra", "tú"),
                             "hubieras dicho")

    def test_conjugate_pluperfect_subjunctive_se1(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the pluperfect subjunctive (-se) tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_se", "yo"),
                             "hubiese hablado")

    def test_conjugate_pluperfect_subjunctive_se2(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ar verb in the pluperfect subjunctive (-se) tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_se", "tú"),
                             "hubieses hablado")

    def test_conjugate_pluperfect_subjunctive_se3(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the pluperfect subjunctive (-se) tense for the
        pronoun él/ella/Ud."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_se",
                                            "él/ella/Ud."), "hubiese bebido")

    def test_conjugate_pluperfect_subjunctive_se4(self):
        """Verify that the conjugate method correctly conjugates a regular
        -er verb in the pluperfect subjunctive (-se) tense for the
        pronoun nosotros."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_se",
                                            "nosotros"), "hubiésemos bebido")

    def test_conjugate_pluperfect_subjunctive_se5(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the pluperfect subjunctive (-se) tense for the
        pronoun vosotros."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_se",
                                            "vosotros"), "hubieseis vivido")

    def test_conjugate_pluperfect_subjunctive_se6(self):
        """Verify that the conjugate method correctly conjugates a regular
        -ir verb in the pluperfect subjunctive (-se) tense for the
        pronoun ellos/ellas/Uds."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_se",
                             "ellos/ellas/Uds."), "hubiesen vivido")

    def test_conjugate_pluperfect_subjunctive_se7(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the pluperfect subjunctive (-se) tense for the
        pronoun yo."""
        with self.app.app_context():
            verb = Verb("hacer")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_se", "yo"),
                             "hubiese hecho")

    def test_conjugate_pluperfect_subjunctive_se8(self):
        """Verify that the conjugate method correctly conjugates an
        irregular verb in the pluperfect subjunctive (-se) tense for the
        pronoun tú."""
        with self.app.app_context():
            verb = Verb("decir")
            self.assertEqual(verb.conjugate("pluperfect_subjunctive_se", "tú"),
                             "hubieses dicho")


if __name__ == "__main__":
    unittest.main()
