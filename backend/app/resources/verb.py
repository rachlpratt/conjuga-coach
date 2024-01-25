from backend.app.models import IrregularVerb, RegularVerb, Tense, Conjugation
from backend.app.utils import conjugate
from backend.app.utils import PRONOUNS, is_valid_tense, is_valid_pronoun


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
        regular_verb = RegularVerb.query.filter_by(
            infinitive=infinitive.lower()).first()
        irregular_verb = IrregularVerb.query.filter_by(
            infinitive=infinitive.lower()).first()
        if not regular_verb and not irregular_verb:
            raise ValueError(f"Invalid verb: {infinitive}")
        self._infinitive = infinitive
        self._is_regular = bool(regular_verb)

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
        return self._is_regular

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

        # Return error if tense is imperative and pronoun is "yo"
        if "imperative" in tense and pronoun == "yo":
            raise ValueError("No first person conjugation for imperative tense")

        # Get pronoun index
        pronoun_index = PRONOUNS.index(pronoun)

        # Account for compound tenses
        compound_tenses = ["present_progressive", "past_progressive",
                           "present_perfect", "pluperfect", "future_perfect",
                           "present_perfect_subjunctive",
                           "pluperfect_subjunctive_ra",
                           "pluperfect_subjunctive_se"]

        # Get tense from database
        tense_obj = Tense.query.filter_by(name=tense).first()
        if not tense_obj and tense not in compound_tenses:
            raise ValueError("Invalid tense")

        # Get verb from database if irregular
        verb_db_entry = IrregularVerb.query.filter_by(
            infinitive=self._infinitive.lower()).first()

        if tense in compound_tenses:
            # Handle compound tenses
            func_name = f'conjugate_{tense}'
            if hasattr(conjugate, func_name) and callable(
                    conjugation_func := getattr(conjugate, func_name)):
                if verb_db_entry:
                    # Try to get participles for irregular verbs from database
                    participles = Conjugation.query.filter_by(
                        verb_id=verb_db_entry.id,
                        tense_id=Tense.query.filter_by(
                            name='participles').first().id).first()
                    if participles:
                        # Use the participle from the database if available
                        participle = (
                            participles.present_participle if
                            "progressive" in tense
                            else participles.past_participle)
                        return conjugation_func(self, pronoun, participle)

                # Fallback to regular verb conjugation if participles not found
                return conjugation_func(self, pronoun)
            else:
                raise ValueError(f"Conjugation function not found for {tense}")

        else:
            # Handle non-compound tenses
            if verb_db_entry:
                # Try to find conjugation for irregular verb
                conjugation = Conjugation.query.filter_by(
                    verb_id=verb_db_entry.id, tense_id=tense_obj.id).first()
                if conjugation:
                    # Map pronoun index to corresponding attribute name
                    pronoun_attributes = ['first_s', 'second_s', 'third_s',
                                          'first_p', 'second_p', 'third_p']
                    if pronoun_index < len(pronoun_attributes):
                        attribute_name = pronoun_attributes[pronoun_index]
                        return getattr(conjugation, attribute_name)

            # Fallback to regular verb conjugation if not found in database
            func_name = f'conjugate_{tense}'
            if hasattr(conjugate, func_name) and callable(
                    conjugation_func := getattr(conjugate, func_name)):
                return conjugation_func(self, pronoun)
            else:
                raise ValueError(f"Conjugation function not found for {tense}")

    def __str__(self) -> str:
        """Get the string representation of the Verb object."""
        return f"Verb: {self.infinitive}"
