import unittest
from quiz import QuizItem
from verb import Verb


class TestQuizItemCreation(unittest.TestCase):
    def test_quiz_item_type(self):
        """Verifies that newly created QuizItem has object type QuizItem."""
        verb = Verb("hacer")
        quiz_item = QuizItem((verb, "present", "yo"), "hago")
        self.assertIsInstance(quiz_item, QuizItem)

    def test_quiz_item_creation1(self):
        """Verifies that newly created QuizItem with valid tense, pronoun, and
        answer but an invalid verb raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            QuizItem(("hacer", "present", "yo"), "hago")
        self.assertEqual(str(context.exception),
                         "Question verb must be type Verb")

    def test_quiz_item_creation2(self):
        """Verifies that newly created QuizItem with valid verb, pronoun, and
        answer but an invalid tense raises a ValueError."""
        verb = Verb("hacer")
        with self.assertRaises(ValueError) as context:
            QuizItem((verb, "abcd", "yo"), "hago")
        self.assertEqual(str(context.exception),
                         "Question tense is not valid")

    def test_quiz_item_creation3(self):
        """Verifies that newly created QuizItem with valid verb, tense, and
        answer but an invalid pronoun raises a ValueError."""
        verb = Verb("hacer")
        with self.assertRaises(ValueError) as context:
            QuizItem((verb, "present", "abcd"), "hago")
        self.assertEqual(str(context.exception),
                         "Question pronoun is not valid")

    def test_quiz_item_creation4(self):
        """Verifies that newly created QuizItem with valid verb, tense, and
        pronoun but an invalid answer raises a ValueError."""
        verb = Verb("hacer")
        invalid_answer = "haces"
        with self.assertRaises(ValueError) as context:
            QuizItem((verb, "present", "yo"), invalid_answer)
        self.assertEqual(str(context.exception),
                         f"Invalid answer: {invalid_answer}")

    def test_quiz_item_creation5(self):
        """Verifies that newly created QuizItem with an invalid question
        tuple containing only two elements raises a ValueError."""
        verb = Verb("hacer")
        with self.assertRaises(ValueError) as context:
            QuizItem((verb, "present"), "hago")
        self.assertEqual(str(context.exception),
                         "Question must be tuple with 3 elements: "
                         "Verb, tense, pronoun")

    def test_quiz_item_creation6(self):
        """Verifies that newly created QuizItem with an invalid question
        containing only a Verb raises a ValueError."""
        verb = Verb("hacer")
        with self.assertRaises(ValueError) as context:
            QuizItem(verb, "hago")
        self.assertEqual(str(context.exception),
                         "Question must be tuple with 3 elements: "
                         "Verb, tense, pronoun")
