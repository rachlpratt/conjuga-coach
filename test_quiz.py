import unittest
from quiz import QuizItem, Quiz
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

    def test_quiz_item_question_verb1(self):
        """Verifies that the question_verb property returns the correct value
        for the QuizItem object."""
        verb = Verb("hacer")
        quiz_item = QuizItem((verb, "present", "yo"), "hago")
        self.assertEqual(verb, quiz_item.question_verb)

    def test_quiz_item_question_verb2(self):
        """Verifies that the question_verb property returns the correct value
        for the QuizItem object."""
        verb = Verb("ir")
        quiz_item = QuizItem((verb, "present", "tú"), "vas")
        self.assertEqual(verb, quiz_item.question_verb)

    def test_quiz_item_question_tense1(self):
        """Verifies that the question_tense property returns the correct value
        for the QuizItem object."""
        verb = Verb("hacer")
        quiz_item = QuizItem((verb, "present", "yo"), "hago")
        self.assertEqual("present", quiz_item.question_tense)

    def test_quiz_item_question_tense2(self):
        """Verifies that the question_tense property returns the correct value
        for the QuizItem object."""
        verb = Verb("ser")
        quiz_item = QuizItem((verb, "preterite", "nosotros"), "fuimos")
        self.assertEqual("preterite", quiz_item.question_tense)

    def test_quiz_item_question_pronoun1(self):
        """Verifies that the question_pronoun property returns the correct
        value for the QuizItem object."""
        verb = Verb("hacer")
        quiz_item = QuizItem((verb, "present", "yo"), "hago")
        self.assertEqual("yo", quiz_item.question_pronoun)

    def test_quiz_item_question_pronoun2(self):
        """Verifies that the question_pronoun property returns the correct
        value for the QuizItem object."""
        verb = Verb("ir")
        quiz_item = QuizItem((verb, "present", "tú"), "vas")
        self.assertEqual("tú", quiz_item.question_pronoun)

    def test_quiz_item_answer1(self):
        """Verifies that the answer property returns the correct value
        for the QuizItem object."""
        verb = Verb("hacer")
        quiz_item = QuizItem((verb, "present", "yo"), "hago")
        self.assertEqual("hago", quiz_item.answer)

    def test_quiz_item_answer2(self):
        """Verifies that the answer property returns the correct value
        for the QuizItem object."""
        verb = Verb("ser")
        quiz_item = QuizItem((verb, "preterite", "tú"), "fuiste")
        self.assertEqual("fuiste", quiz_item.answer)

    def test_str_method(self):
        """Verifies that the __str__ method returns the expected string
        representation for a QuizItem object."""
        verb = Verb("hacer")
        quiz_item = QuizItem((verb, "present", "yo"), "hago")
        self.assertEqual(str(quiz_item), "Question: yo hacer (present)\n"
                                         "Answer: hago")


class TestQuizCreation(unittest.TestCase):
    def test_quiz_type(self):
        """Verifies that newly created Quiz has object type Quiz."""
        verb1 = Verb("hacer")
        verb2 = Verb("ir")
        quiz = Quiz([verb1, verb2], ["present", "preterite"], ["yo", "tú"])
        self.assertIsInstance(quiz, Quiz)

    def test_quiz_creation1(self):
        """Verifies that newly created Quiz with a valid tense_list and
        pronoun_list but an invalid verb_list raises a ValueError."""
        verb_list = ["hacer", "decir"]
        tense_list = ["present", "preterite"]
        pronoun_list = ["yo", "tú"]
        with self.assertRaises(ValueError) as context:
            Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(str(context.exception),
                         "verb_list must be a list of valid Verb objects")

    def test_quiz_creation2(self):
        """Verifies that newly created Quiz with a valid tense_list and
        pronoun_list but an invalid verb_list raises a ValueError."""
        verb_list = Verb("hacer")
        tense_list = ["present", "preterite"]
        pronoun_list = ["yo", "tú"]
        with self.assertRaises(ValueError) as context:
            Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(str(context.exception),
                         "verb_list must be a list of valid Verb objects")

    def test_quiz_creation3(self):
        """Verifies that newly created Quiz with a valid verb_list and
        pronoun_list but an invalid tense_list raises a ValueError."""
        verb1 = Verb("hacer")
        verb2 = Verb("ir")
        verb_list = [verb1, verb2]
        tense_list = ["present", "abcd"]
        pronoun_list = ["yo", "tú"]
        with self.assertRaises(ValueError) as context:
            Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(str(context.exception),
                         "tense_list must be a list of valid tenses")

    def test_quiz_creation4(self):
        """Verifies that newly created Quiz with a valid verb_list and
        pronoun_list but an invalid tense_list raises a ValueError."""
        verb1 = Verb("hacer")
        verb2 = Verb("ir")
        verb_list = [verb1, verb2]
        tense_list = "present"
        pronoun_list = ["yo", "tú"]
        with self.assertRaises(ValueError) as context:
            Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(str(context.exception),
                         "tense_list must be a list of valid tenses")

    def test_quiz_creation5(self):
        """Verifies that newly created Quiz with a valid verb_list and
        tense_list but an invalid pronoun_list raises a ValueError."""
        verb1 = Verb("hacer")
        verb2 = Verb("ir")
        verb_list = [verb1, verb2]
        tense_list = ["present", "preterite"]
        pronoun_list = ["yo", "abcd"]
        with self.assertRaises(ValueError) as context:
            Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(str(context.exception),
                         "pronoun_list must be a list of valid pronouns")

    def test_quiz_creation6(self):
        """Verifies that newly created Quiz with a valid verb_list and
        tense_list but an invalid pronoun_list raises a ValueError."""
        verb1 = Verb("hacer")
        verb2 = Verb("ir")
        verb_list = [verb1, verb2]
        tense_list = ["present", "preterite"]
        pronoun_list = 4
        with self.assertRaises(ValueError) as context:
            Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(str(context.exception),
                         "pronoun_list must be a list of valid pronouns")

    def test_quiz_verb_list(self):
        """Verifies that the verb_list property returns the correct value
        for the Quiz object."""
        verb1 = Verb("hacer")
        verb2 = Verb("decir")
        verb_list = [verb1, verb2]
        tense_list = ["present", "imperfect"]
        pronoun_list = ["yo", "tú"]
        quiz = Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(verb_list, quiz.verb_list)

    def test_quiz_tense_list(self):
        """Verifies that the tense_list property returns the correct value
        for the Quiz object."""
        verb1 = Verb("hacer")
        verb2 = Verb("decir")
        verb_list = [verb1, verb2]
        tense_list = ["present", "imperfect"]
        pronoun_list = ["yo", "tú"]
        quiz = Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(tense_list, quiz.tense_list)

    def test_quiz_pronoun_list(self):
        """Verifies that the pronoun_list property returns the correct value
        for the Quiz object."""
        verb1 = Verb("hacer")
        verb2 = Verb("decir")
        verb_list = [verb1, verb2]
        tense_list = ["present", "imperfect"]
        pronoun_list = ["yo", "tú"]
        quiz = Quiz(verb_list, tense_list, pronoun_list)
        self.assertEqual(pronoun_list, quiz.pronoun_list)
