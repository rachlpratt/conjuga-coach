import unittest
from quiz import QuizItem
from verb import Verb


class TestQuizItemCreation(unittest.TestCase):
    def test_quiz_item_type(self):
        """Verifies that newly created QuizItem has object type QuizItem."""
        verb = Verb("hacer")
        quiz_item = QuizItem((verb, "present", "yo"), "hago")
        self.assertIsInstance(quiz_item, QuizItem)
