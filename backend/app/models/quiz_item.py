from backend.app.models import Verb
from backend.app.utils import is_valid_tense, is_valid_pronoun


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
