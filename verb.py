from utils import PRONOUNS, is_valid_tense, is_valid_pronoun
import conjugate
from regular_verbs import regular_verbs
from irregular_verbs import irregular_verbs


class Verb:
    def __init__(self, infinitive: str) -> None:
        """Initialize a Verb object."""
        self.infinitive = infinitive

    @property
    def infinitive(self) -> str:
        """Get the infinitive form of the verb."""
        return self._infinitive

    @infinitive.setter
    def infinitive(self, infinitive: str) -> None:
        """
        Set the infinitive form of the verb.

        Raises:
            ValueError: if the infinitive is not a valid verb.
        """
        if infinitive.lower() not in regular_verbs and \
                infinitive.lower() not in irregular_verbs:
            raise ValueError(f"Invalid verb: {infinitive}")
        self._infinitive = infinitive

    @property
    def stem(self) -> str:
        """Get the stem of a verb."""
        return self._infinitive[:-2]

    @property
    def ending(self) -> str:
        """Get the ending of a verb."""
        endings = ["ar", "er", "ir"]
        if self._infinitive[-2:] in endings:
            return self._infinitive[-2:]

    @property
    def is_regular(self) -> bool:
        """Return True if the verb is regular, otherwise return False."""
        return self._infinitive in regular_verbs

    def conjugate(self, tense: str, pronoun: str) -> str:
        """
        Conjugate the verb with a given tense and pronoun.

        Raises:
            ValueError: if the tense or pronoun is invalid.
        """
        # Validate tense and pronoun
        if not is_valid_tense(tense):
            raise ValueError("Invalid tense")
        if not is_valid_pronoun(pronoun):
            raise ValueError("Invalid pronoun")

        # Get pronoun index
        pronoun_index = PRONOUNS.index(pronoun)

        # Pull conjugation from irregular verbs dict if irregular
        try:
            return irregular_verbs[self.infinitive][tense][pronoun_index]

        # Conjugate by calling correct function
        except KeyError:
            func_name = f'conjugate_{tense}'
            if hasattr(conjugate, func_name) and \
                    callable(conjugation_func := getattr(conjugate, func_name)):
                return conjugation_func(self, pronoun)

    def __str__(self) -> str:
        """Get the string representation of the Verb object."""
        return f"Verb: {self.infinitive}"
