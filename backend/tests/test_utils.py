import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from backend.app.extensions import db
from backend.app.resources.verb import Verb
from backend.app.utils import (is_valid_tense, is_valid_pronoun,
                       get_present_participle, get_past_participle)
from backend.tests.setup_tests import setup_testing_db


class TestUtils(unittest.TestCase):
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

    def test_is_valid_tense1(self):
        """Verify that is_valid_tense returns True given a valid tense."""
        self.assertTrue(is_valid_tense("present"))

    def test_is_valid_tense2(self):
        """Verify that is_valid_tense returns False given an invalid tense."""
        self.assertTrue(is_valid_tense("present"))
        self.assertFalse(is_valid_tense("abcd"))

    def test_is_valid_tense3(self):
        """Verify that is_valid_tense returns False given an invalid,
        non-string tense."""
        self.assertFalse(is_valid_tense(1))

    def test_is_valid_tense4(self):
        """Verify that is_valid_tense returns False given an invalid,
        empty string tense."""
        self.assertFalse(is_valid_tense(""))

    def test_is_valid_pronoun1(self):
        """Verify that is_valid_pronoun returns True given a valid pronoun."""
        self.assertTrue(is_valid_pronoun("yo"))

    def test_is_valid_pronoun2(self):
        """Verify that is_valid_pronoun returns True given a valid pronoun."""
        self.assertTrue(is_valid_pronoun("vosotros"))

    def test_is_valid_pronoun3(self):
        """Verify that is_valid_pronoun returns False given an  invalid
        pronoun."""
        self.assertFalse(is_valid_pronoun("abcd"))

    def test_is_valid_pronoun4(self):
        """Verify that is_valid_pronoun returns False given an invalid,
        non-string pronoun."""
        self.assertFalse(is_valid_pronoun(2))

    def test_is_valid_pronoun5(self):
        """Verify that is_valid_pronoun returns False given an invalid,
        empty string pronoun."""
        self.assertFalse(is_valid_pronoun(""))

    def test_get_present_participle1(self):
        """Verify that get_present_participle returns the correct present
        participle given a regular -ar verb."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(get_present_participle(verb), "hablando")

    def test_get_present_participle2(self):
        """Verify that get_present_participle returns the correct present
        participle given a regular -er verb."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(get_present_participle(verb), "bebiendo")

    def test_get_present_participle3(self):
        """Verify that get_present_participle returns the correct present
        participle given a regular -ir verb."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(get_present_participle(verb), "viviendo")

    def test_get_past_participle1(self):
        """Verify that get_past_participle returns the correct past
        participle given a regular -ar verb."""
        with self.app.app_context():
            verb = Verb("hablar")
            self.assertEqual(get_past_participle(verb), "hablado")

    def test_get_past_participle2(self):
        """Verify that get_past_participle returns the correct past
        participle given a regular -er verb."""
        with self.app.app_context():
            verb = Verb("beber")
            self.assertEqual(get_past_participle(verb), "bebido")

    def test_get_past_participle3(self):
        """Verify that get_past_participle returns the correct past
        participle given a regular -ir verb."""
        with self.app.app_context():
            verb = Verb("vivir")
            self.assertEqual(get_past_participle(verb), "vivido")


if __name__ == "__main__":
    unittest.main()
