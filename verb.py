from utils import PRONOUNS
import conjugate
from regular_verbs import regular_verbs
from irregular_verbs import irregular_verbs


class Verb:
    def __init__(self, infinitive):
        if not self.is_valid(infinitive):
            raise ValueError(f"Invalid verb: {infinitive}")
        self._infinitive = infinitive

    @property
    def infinitive(self):
        return self._infinitive

    @property
    def stem(self):
        return self._infinitive[:-2]

    @property
    def ending(self):
        endings = ["ar", "er", "ir"]
        if self._infinitive[-2:] in endings:
            return self._infinitive[-2:]

    @property
    def is_regular(self):
        return self._infinitive in regular_verbs

    @classmethod
    def is_valid(cls, infinitive):
        return infinitive in regular_verbs or infinitive in irregular_verbs

    def conjugate(self, tense, pronoun):
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

    def __str__(self):
        return f"Verb: {self._infinitive}"
