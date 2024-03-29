import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from backend.app.extensions import db
from backend.app.resources.verb import Verb
from backend.app.resources.quiz import Quiz
from backend.app.resources.quiz_item import QuizItem
from backend.tests.setup_tests import setup_testing_db


class TestQuizItemCreation(unittest.TestCase):
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

    def test_quiz_item_type(self):
        """Verify that newly created QuizItem has object type QuizItem."""
        with self.app.app_context():
            verb = Verb("hacer")
            quiz_item = QuizItem((verb, "present", "yo"), "hago")
            self.assertIsInstance(quiz_item, QuizItem)

    def test_quiz_item_creation1(self):
        """Verify that newly created QuizItem with valid tense, pronoun, and
        answer but an invalid verb raises a ValueError."""
        with self.app.app_context():
            with self.assertRaises(ValueError) as context:
                QuizItem(("hacer", "present", "yo"), "hago")
            self.assertEqual(str(context.exception),
                             "Question verb must be type Verb")

    def test_quiz_item_creation2(self):
        """Verify that newly created QuizItem with valid verb, pronoun, and
        answer but an invalid tense raises a ValueError."""
        with self.app.app_context():
            verb = Verb("hacer")
            with self.assertRaises(ValueError) as context:
                QuizItem((verb, "abcd", "yo"), "hago")
            self.assertEqual(str(context.exception),
                             "Question tense is not valid")

    def test_quiz_item_creation3(self):
        """Verify that newly created QuizItem with valid verb, tense, and
        answer but an invalid pronoun raises a ValueError."""
        with self.app.app_context():
            verb = Verb("hacer")
            with self.assertRaises(ValueError) as context:
                QuizItem((verb, "present", "abcd"), "hago")
            self.assertEqual(str(context.exception),
                             "Question pronoun is not valid")

    def test_quiz_item_creation4(self):
        """Verify that newly created QuizItem with valid verb, tense, and
        pronoun but an invalid answer raises a ValueError."""
        with self.app.app_context():
            verb = Verb("hacer")
            invalid_answer = "haces"
            with self.assertRaises(ValueError) as context:
                QuizItem((verb, "present", "yo"), invalid_answer)
            self.assertEqual(str(context.exception),
                             f"Invalid answer: {invalid_answer}")

    def test_quiz_item_creation5(self):
        """Verify that newly created QuizItem with an invalid question tuple
        containing only two elements raises a ValueError."""
        with self.app.app_context():
            verb = Verb("hacer")
            with self.assertRaises(ValueError) as context:
                QuizItem((verb, "present"), "hago")
            self.assertEqual(str(context.exception),
                             "Question must be tuple with 3 elements: "
                             "Verb, tense, pronoun")

    def test_quiz_item_creation6(self):
        """Verify that newly created QuizItem with an invalid question
        containing only a Verb raises a ValueError."""
        with self.app.app_context():
            verb = Verb("hacer")
            with self.assertRaises(ValueError) as context:
                QuizItem(verb, "hago")
            self.assertEqual(str(context.exception),
                             "Question must be tuple with 3 elements: "
                             "Verb, tense, pronoun")

    def test_quiz_item_question_verb1(self):
        """Verify that the question_verb property returns the correct value
        for the QuizItem object."""
        with self.app.app_context():
            verb = Verb("hacer")
            quiz_item = QuizItem((verb, "present", "yo"), "hago")
            self.assertEqual(verb, quiz_item.question_verb)

    def test_quiz_item_question_verb2(self):
        """Verify that the question_verb property returns the correct value
        for the QuizItem object."""
        with self.app.app_context():
            verb = Verb("ir")
            quiz_item = QuizItem((verb, "present", "tú"), "vas")
            self.assertEqual(verb, quiz_item.question_verb)

    def test_quiz_item_question_tense1(self):
        """Verify that the question_tense property returns the correct value
        for the QuizItem object."""
        with self.app.app_context():
            verb = Verb("hacer")
            quiz_item = QuizItem((verb, "present", "yo"), "hago")
            self.assertEqual("present", quiz_item.question_tense)

    def test_quiz_item_question_tense2(self):
        """Verify that the question_tense property returns the correct value
        for the QuizItem object."""
        with self.app.app_context():
            verb = Verb("ser")
            quiz_item = QuizItem((verb, "preterite", "nosotros"), "fuimos")
            self.assertEqual("preterite", quiz_item.question_tense)

    def test_quiz_item_question_pronoun1(self):
        """Verify that the question_pronoun property returns the correct value
        for the QuizItem object."""
        with self.app.app_context():
            verb = Verb("hacer")
            quiz_item = QuizItem((verb, "present", "yo"), "hago")
            self.assertEqual("yo", quiz_item.question_pronoun)

    def test_quiz_item_question_pronoun2(self):
        """Verify that the question_pronoun property returns the correct value
        for the QuizItem object."""
        with self.app.app_context():
            verb = Verb("ir")
            quiz_item = QuizItem((verb, "present", "tú"), "vas")
            self.assertEqual("tú", quiz_item.question_pronoun)

    def test_quiz_item_answer1(self):
        """Verify that the answer property returns the correct value for the
        QuizItem object."""
        with self.app.app_context():
            verb = Verb("hacer")
            quiz_item = QuizItem((verb, "present", "yo"), "hago")
            self.assertEqual("hago", quiz_item.answer)

    def test_quiz_item_answer2(self):
        """Verify that the answer property returns the correct value for the
        QuizItem object."""
        with self.app.app_context():
            verb = Verb("ser")
            quiz_item = QuizItem((verb, "preterite", "tú"), "fuiste")
            self.assertEqual("fuiste", quiz_item.answer)

    def test_quiz_item_str_method(self):
        """Verify that the __str__ method returns the expected string
        representation for a QuizItem object."""
        with self.app.app_context():
            verb = Verb("hacer")
            quiz_item = QuizItem((verb, "present", "yo"), "hago")
            self.assertEqual(str(quiz_item), "Question: yo hacer (present)\n"
                                             "Answer: hago")

    def test_quiz_type(self):
        """Verify that newly created Quiz has object type Quiz."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("ir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertIsInstance(quiz, Quiz)

    def test_quiz_creation1(self):
        """Verify that newly created Quiz with a valid tense_list and
        pronoun_list but an invalid verb_list raises a ValueError."""
        with self.app.app_context():
            verb_list = ["hacer", "decir"]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(str(context.exception),
                             "verb_list must be a list of valid Verb objects")

    def test_quiz_creation2(self):
        """Verify that newly created Quiz with a valid tense_list and
        pronoun_list but an invalid verb_list raises a ValueError."""
        with self.app.app_context():
            verb_list = Verb("hacer")
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(str(context.exception),
                             "verb_list must be a list of valid Verb objects")

    def test_quiz_creation3(self):
        """Verify that newly created Quiz with a valid verb_list and
        pronoun_list but an invalid tense_list raises a ValueError."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("ir")]
            tense_list = ["present", "abcd"]
            pronoun_list = ["yo", "tú"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(str(context.exception),
                             "tense_list must be a list of valid tenses")

    def test_quiz_creation4(self):
        """Verify that newly created Quiz with a valid verb_list and
        pronoun_list but an invalid tense_list raises a ValueError."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("ir")]
            tense_list = "present"
            pronoun_list = ["yo", "tú"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(str(context.exception),
                             "tense_list must be a list of valid tenses")

    def test_quiz_creation5(self):
        """Verify that newly created Quiz with a valid verb_list and
        tense_list but an invalid pronoun_list raises a ValueError."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("ir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "abcd"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(str(context.exception),
                             "pronoun_list must be a list of valid pronouns")

    def test_quiz_creation6(self):
        """Verify that newly created Quiz with a valid verb_list and
        tense_list but an invalid pronoun_list raises a ValueError."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("ir")]
            tense_list = ["present", "preterite"]
            pronoun_list = 4
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(str(context.exception),
                             "pronoun_list must be a list of valid pronouns")

    def test_quiz_creation7(self):
        """Verify that creating a Quiz with valid lists but an invalid
        num_items of 0 raises a ValueError."""
        with self.app.app_context():
            verb_list = [Verb("hacer")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú", "nosotros"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list, 0)
            self.assertEqual(str(context.exception),
                             "num_items must be an int between 1 and 50, "
                             "or None")

    def test_quiz_creation8(self):
        """Verify that creating a Quiz with valid lists but an invalid
        num_items of -1 raises a ValueError."""
        with self.app.app_context():
            verb_list = [Verb("hacer")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú", "nosotros"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list, -1)
            self.assertEqual(str(context.exception),
                             "num_items must be an int between 1 and 50, "
                             "or None")

    def test_quiz_creation9(self):
        """Verify that creating a Quiz with valid lists but an invalid
        num_items of 101 raises a ValueError."""
        with self.app.app_context():
            verb_list = [Verb("hacer")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú", "nosotros"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list, 51)
            self.assertEqual(str(context.exception),
                             "num_items must be an int between 1 and 50, "
                             "or None")

    def test_quiz_creation10(self):
        """Verify that creating a Quiz with valid lists but an invalid
        num_items of type str raises a ValueError."""
        with self.app.app_context():
            verb_list = [Verb("hacer")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú", "nosotros"]
            with self.assertRaises(ValueError) as context:
                Quiz(verb_list, tense_list, pronoun_list, "abcd")
            self.assertEqual(str(context.exception),
                             "num_items must be an int between 1 and 50, "
                             "or None")

    def test_quiz_verb_list(self):
        """Verify that the verb_list property returns the correct value for
        the Quiz object."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "imperfect"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(verb_list, quiz.verb_list)

    def test_quiz_tense_list(self):
        """Verify that the tense_list property returns the correct value
        for the Quiz object."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "imperfect"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(tense_list, quiz.tense_list)

    def test_quiz_pronoun_list(self):
        """Verify that the pronoun_list property returns the correct value
        for the Quiz object."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "imperfect"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(pronoun_list, quiz.pronoun_list)

    def test_quiz_num_items1(self):
        """Verify that the num_items property returns the correct value
        for the Quiz object when no num_items value is provided (should be
        equal to total number of possible combinations for max of 50)."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(8, quiz.num_items)

    def test_quiz_num_items2(self):
        """Verify that the num_items property returns the correct value
        for the Quiz object when num_items value larger than total number of
        possible combinations is provided (should be equal to total number of
        possible combinations)."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list, 9)
            self.assertEqual(8, quiz.num_items)

    def test_quiz_num_items3(self):
        """Verify that the num_items property returns the correct value
        for the Quiz object when num_items value equal to total number of
        possible combinations is provided (should be equal to num_items)."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list, 8)
            self.assertEqual(8, quiz.num_items)

    def test_quiz_num_items4(self):
        """Verify that the num_items property returns the correct value
        for the Quiz object when num_items value smaller than total number of
        possible combinations is provided (should be equal to num_items)."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list, 5)
            self.assertEqual(5, quiz.num_items)

    def test_quiz_num_items6(self):
        """Verify that the num_items property returns the correct value for
        the Quiz object when provided num_items value is set to lower limit
        of 1."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list, 1)
            self.assertEqual(1, quiz.num_items)

    def test_quiz_num_items7(self):
        """Verify that the num_items property returns the correct value for
        the Quiz object when provided num_items value is set to upper limit
        of 50."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir"), Verb("ir"), Verb("ser")]
            tense_list = ["present", "preterite", "imperfect", "future",
                          "conditional", "present_subjunctive"]
            pronoun_list = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros"]
            quiz = Quiz(verb_list, tense_list, pronoun_list, 50)
            self.assertEqual(50, quiz.num_items)

    def test_quiz_bank1(self):
        """Verify that the quiz_bank property returns a list."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertIsInstance(quiz.quiz_bank, list)

    def test_quiz_bank2(self):
        """Verify that all objects in the quiz_bank property are of type
        QuizItem."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertTrue(all(isinstance(item, QuizItem)
                                for item in quiz.quiz_bank))

    def test_quiz_bank3(self):
        """Verify that the quiz_bank property covers all combinations of
        verb, tense, and pronoun when no num_items is provided."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("decir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            expected_combinations = [(verb, tense, pronoun)
                                     for verb in verb_list
                                     for tense in tense_list
                                     for pronoun in pronoun_list]
            actual_combinations = [(item.question_verb, item.question_tense,
                                    item.question_pronoun)
                                   for item in quiz.quiz_bank]
            self.assertTrue(all(comb in actual_combinations for comb in
                                expected_combinations))

    def test_quiz_str_method(self):
        """Verify that the __str__ method returns the expected string
        representation for a Quiz object."""
        with self.app.app_context():
            verb_list = [Verb("hacer")]
            tense_list = ["present"]
            pronoun_list = ["yo"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(str(quiz), "QUIZ:\n"
                                        "Verbs: Verb: hacer\n"
                                        "Tenses: present\n"
                                        "Pronouns: yo\n"
                                        "Number of Items: 1\n"
                                        "------------\n"
                                        "Quiz Items:\n"
                                        "Question: yo hacer (present)\n"
                                        "Answer: hago")

    def test_quiz_iter_method(self):
        """Verify that the __iter__ method returns the Quiz object itself."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("ir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertEqual(iter(quiz), quiz)

    def test_quiz_next_method(self):
        """Verify that the __next__ method returns a QuizItem instance."""
        with self.app.app_context():
            verb_list = [Verb("hacer"), Verb("ir")]
            tense_list = ["present", "preterite"]
            pronoun_list = ["yo", "tú"]
            quiz = Quiz(verb_list, tense_list, pronoun_list)
            self.assertIsInstance(next(iter(quiz)), QuizItem)


if __name__ == "__main__":
    unittest.main()
