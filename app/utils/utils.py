from app.utils import irregular_verbs

PRONOUNS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros",
            "ellos/ellas/Uds."]


def is_valid_tense(tense):
    """Returns True if the given tense is valid; otherwise, returns False."""
    tenses = ["present", "preterite", "imperfect", "conditional", "future",
              "present_subjunctive", "imperfect_subjunctive_ra",
              "imperfect_subjunctive_se", "present_progressive",
              "past_progressive", "present_perfect", "pluperfect",
              "future_perfect", "present_perfect_subjunctive",
              "pluperfect_subjunctive_ra", "pluperfect_subjunctive_se",
              "affirmative_imperative", "negative_imperative"]
    return tense in tenses


def is_valid_pronoun(pronoun):
    """Returns True if the given pronoun is valid; otherwise, returns False."""
    return pronoun in PRONOUNS


def get_present_participle(verb):
    """Returns the present participle for the given verb."""
    infinitive, stem = verb.infinitive, verb.stem

    # Check if verb has irregular participles
    irregular_participles = \
        irregular_verbs.get(infinitive, {}).get("participles", [])
    if irregular_participles:
        return irregular_participles[0]

    # Return regular present participle
    return stem + ("ando" if verb.ending == "ar" else "iendo")


def get_past_participle(verb):
    """Returns the past participle for the given verb."""
    infinitive, stem = verb.infinitive, verb.stem

    # Check if verb has irregular participles
    irregular_participles = \
        irregular_verbs.get(infinitive, {}).get("participles", [])
    if irregular_participles:
        return irregular_participles[1]

    # Return regular past participle
    return stem + ("ado" if verb.ending == "ar" else "ido")
