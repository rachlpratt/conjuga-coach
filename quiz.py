from verb import Verb
from utils import is_valid_tense, is_valid_pronoun
import random


class QuizItem:
    def __init__(self, question: tuple[Verb, str, str], answer: str) -> None:
        """Initialize a QuizItem with a question and an answer."""
        self._question_verb = None
        self._question_tense = None
        self._question_pronoun = None
        self.update_question(question)
        self.answer = answer

    def update_question(self, question: tuple[Verb, str, str]) -> None:
        """
        Update the question components: verb, tense, and pronoun.

        Raises:
            ValueError: if the question is not a tuple with 3 elements
                        or if any component is invalid.
        """
        if not isinstance(question, tuple) or len(question) != 3:
            raise ValueError("Question must be tuple with 3 elements: "
                             "Verb, tense, pronoun")

        question_verb, question_tense, question_pronoun = question
        if not isinstance(question_verb, Verb):
            raise ValueError("Question verb must be type Verb")

        if not is_valid_tense(question_tense):
            raise ValueError("Question tense is not valid")

        if not is_valid_pronoun(question_pronoun):
            raise ValueError("Question pronoun is not valid")

        self._question_verb = question_verb
        self._question_tense = question_tense
        self._question_pronoun = question_pronoun

    @property
    def question_verb(self) -> Verb:
        """Get the Verb part of the question."""
        return self._question_verb

    @property
    def question_tense(self) -> str:
        """Get the tense part of the question."""
        return self._question_tense

    @property
    def question_pronoun(self) -> str:
        """Get the pronoun part of the question."""
        return self._question_pronoun

    @property
    def answer(self) -> str:
        """Get the answer."""
        return self._answer

    @answer.setter
    def answer(self, answer: str) -> None:
        """
        Set the answer.

        Raises:
            ValueError: if the answer is incorrect for the given question.
        """
        if self._question_verb.conjugate(self._question_tense,
                                         self._question_pronoun) != answer:
            raise ValueError(f"Invalid answer: {answer}")
        self._answer = answer

    def __str__(self) -> str:
        """Get the string representation of the QuizItem object."""
        return f"Question: {self._question_pronoun} " \
               f"{self._question_verb.infinitive} " \
               f"({self._question_tense})\n" \
               f"Answer: {self.answer}"


class Quiz:
    def __init__(self, verb_list: list[Verb], tense_list: list[str],
                 pronoun_list: list[str], num_items: int = None) -> None:
        """Initialize a Quiz object with lists of verbs, tenses, and pronouns."""
        self.verb_list = verb_list
        self.tense_list = tense_list
        self.pronoun_list = pronoun_list
        self.num_items = num_items
        self.quiz_bank = self.create_quiz_bank()

    @property
    def verb_list(self) -> list:
        """Get the verb_list."""
        return self._verb_list

    @verb_list.setter
    def verb_list(self, verb_list: list) -> None:
        """
        Set the verb_list.

        Raises:
            ValueError: if the verb_list is invalid.
        """
        if not isinstance(verb_list, list) or not all(
                isinstance(verb, Verb) for
                verb in verb_list
        ):
            raise ValueError("verb_list must be a list of valid Verb objects")
        self._verb_list = verb_list

    @property
    def tense_list(self) -> list:
        """Get the tense_list."""
        return self._tense_list

    @tense_list.setter
    def tense_list(self, tense_list: list) -> None:
        """
        Set the tense_list.

        Raises:
            ValueError: if the tense_list is invalid.
        """
        if not isinstance(tense_list, list) or not all(
                isinstance(tense, str) and is_valid_tense(tense) for
                tense in tense_list
        ):
            raise ValueError("tense_list must be a list of valid tenses")
        self._tense_list = tense_list

    @property
    def pronoun_list(self) -> list:
        """Get the pronoun_list."""
        return self._pronoun_list

    @pronoun_list.setter
    def pronoun_list(self, pronoun_list: list) -> None:
        """
        Set the pronoun_list.

        Raises:
            ValueError: if the pronoun_list is invalid.
        """
        if not isinstance(pronoun_list, list) or not all(
                isinstance(pronoun, str) and is_valid_pronoun(pronoun) for
                pronoun in pronoun_list
        ):
            raise ValueError("pronoun_list must be a list of valid pronouns")
        self._pronoun_list = pronoun_list

    @property
    def num_items(self) -> int | None:
        """Get the number of quiz items."""
        return self._num_items

    @num_items.setter
    def num_items(self, num_items: int | None) -> None:
        """Set the number of quiz items."""
        if num_items is not None and \
                (not isinstance(num_items, int) or not 1 <= num_items <= 100):
            raise ValueError("num_items must be an int between 1 and 100, "
                             "or None")
        self._num_items = num_items

    @property
    def quiz_bank(self) -> list:
        """Get the quiz_bank."""
        return self._quiz_bank

    @quiz_bank.setter
    def quiz_bank(self, quiz_bank: list) -> None:
        """Set the quiz_bank."""
        if not isinstance(quiz_bank, list) or not \
                all(isinstance(item, QuizItem) for item in quiz_bank):
            raise ValueError("quiz_bank must be a list of QuizItem objects")
        self._quiz_bank = quiz_bank

    def create_quiz_bank(self) -> list:
        """Create a quiz_bank based on the verb, tense, and pronoun lists."""
        quiz_bank = []
        for verb in self.verb_list:
            for tense in self.tense_list:
                for pronoun in self.pronoun_list:
                    question = (verb, tense, pronoun)
                    answer = verb.conjugate(tense, pronoun)
                    quiz_item = QuizItem(question, answer)
                    quiz_bank.append(quiz_item)

        # Update num_items if not provided or if it exceeds size of quiz_bank
        total_items = len(quiz_bank)
        if self.num_items is None or self.num_items > total_items:
            self.num_items = min(total_items, 100)
        return random.sample(quiz_bank, self.num_items)
