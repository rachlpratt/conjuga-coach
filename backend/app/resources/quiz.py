import random

from .quiz_item import QuizItem
from .verb import Verb
from backend.app.utils import is_valid_tense, is_valid_pronoun


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
                (not isinstance(num_items, int) or not 1 <= num_items <= 50):
            raise ValueError("num_items must be an int between 1 and 50, "
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
                    if pronoun == "yo" and "imperative" in tense:
                        continue
                    question = (verb, tense, pronoun)
                    answer = verb.conjugate(tense, pronoun)
                    quiz_item = QuizItem(question, answer)
                    quiz_bank.append(quiz_item)

        # Update num_items if not provided or if it exceeds size of quiz_bank
        total_items = len(quiz_bank)
        if self.num_items is None or self.num_items > total_items:
            self.num_items = min(total_items, 50)
        return random.sample(quiz_bank, self.num_items)

    def __str__(self) -> str:
        """Get the string representation of the Quiz object."""
        verb_str = ", ".join(str(verb) for verb in self.verb_list)
        tense_str = ", ".join(self.tense_list)
        pronoun_str = ", ".join(self.pronoun_list)

        quiz_items_str = "\n".join(str(item) for item in self.quiz_bank)

        return (f"QUIZ:\n"
                f"Verbs: {verb_str}\n"
                f"Tenses: {tense_str}\n"
                f"Pronouns: {pronoun_str}\n"
                f"Number of Items: {self.num_items}\n"
                f"------------\n"
                f"Quiz Items:\n{quiz_items_str}")

    def __iter__(self):
        """Initialize iterator and return the Quiz object itself."""
        self._current_index = 0
        return self

    def __next__(self):
        """Return the next QuizItem in the sequence or raise StopIteration."""
        if self._current_index < len(self.quiz_bank):
            item = self.quiz_bank[self._current_index]
            self._current_index += 1
            return item
        else:
            raise StopIteration
