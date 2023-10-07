PRONOUNS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros",
            "ellos/ellas/Uds."]


def is_valid_tense(tense):
    """Returns True if the given tense is valid; otherwise, returns False"""
    tenses = ["present", "preterite", "imperfect", "conditional", "future",
              "present_subjunctive", "imperfect_subjunctive_ra",
              "imperfect_subjunctive_se", "present_progressive",
              "past_progressive", "present_perfect", "pluperfect",
              "future_perfect", "present_perfect_subjunctive",
              "pluperfect_subjunctive_ra", "pluperfect_subjunctive_se",
              "affirmative_imperative", "negative_imperative"]
    return tense in tenses


def is_valid_pronoun(pronoun):
    """Returns True if the given pronoun is valid; otherwise, returns False"""
    return pronoun in PRONOUNS
