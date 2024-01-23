from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.resources.verb import Verb

PRONOUNS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros",
            "ellos/ellas/Uds."]


def is_valid_tense(tense: str) -> bool:
    """Returns True if the given tense is valid; otherwise, returns False."""
    tenses = ["present", "preterite", "imperfect", "conditional", "future",
              "present_subjunctive", "imperfect_subjunctive_ra",
              "imperfect_subjunctive_se", "present_progressive",
              "past_progressive", "present_perfect", "pluperfect",
              "future_perfect", "present_perfect_subjunctive",
              "pluperfect_subjunctive_ra", "pluperfect_subjunctive_se",
              "affirmative_imperative", "negative_imperative"]
    return tense in tenses


def is_valid_pronoun(pronoun: str) -> bool:
    """Returns True if the given pronoun is valid; otherwise, returns False."""
    return pronoun in PRONOUNS


def get_present_participle(verb: 'Verb') -> str:
    """Returns the regular present participle for the given verb."""
    infinitive, stem = verb.infinitive, verb.stem
    return stem + ("ando" if verb.ending == "ar" else "iendo")


def get_past_participle(verb: 'Verb') -> str:
    """Returns the regular past participle for the given verb."""
    infinitive, stem = verb.infinitive, verb.stem
    return stem + ("ado" if verb.ending == "ar" else "ido")
