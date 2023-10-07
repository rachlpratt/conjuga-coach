from irregular_verbs import irregular_verbs

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
    try:
        return irregular_verbs[infinitive]["participles"][0]
    except KeyError:
        if verb.ending == "ar":
            return stem + "ando"
        else:
            return stem + "iendo"


def get_past_participle(verb):
    """Returns the past participle for the given verb."""
    infinitive, stem = verb.infinitive, verb.stem
    try:
        return irregular_verbs[infinitive]["participles"][1]
    except KeyError:
        if verb.ending == "ar":
            return stem + "ado"
        else:
            return stem + "ido"
