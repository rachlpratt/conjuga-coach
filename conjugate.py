def conjugate_present(verb, pronoun):
    infinitive, stem = verb.infinitive, verb.stem
    match pronoun:
        case "yo":
            return stem + "o"
        case "tú":
            if verb.ending == "ar":
                return stem + "as"
            else:
                return stem + "es"
        case "él/ella/Ud.":
            if verb.ending == "ar":
                return stem + "a"
            else:
                return stem + "e"
        case "nosotros":
            return stem + infinitive[-2] + "mos"
        case "vosotros":
            if verb.ending == "ar":
                return stem + "áis"
            elif verb.ending == "er":
                return stem + "éis"
            else:
                return stem + "ís"
        case "ellos/ellas/Uds.":
            if verb.ending == "ar":
                return stem + "an"
            else:
                return stem + "en"


def conjugate_preterite(verb, pronoun):
    stem = verb.stem
    match pronoun:
        case "yo":
            if verb.ending == "ar":
                return stem + "é"
            else:
                return stem + "í"
        case "tú":
            if verb.ending == "ar":
                return stem + "aste"
            else:
                return stem + "iste"
        case "él/ella/Ud.":
            if verb.ending == "ar":
                return stem + "ó"
            else:
                return stem + "ió"
        case "nosotros":
            if verb.ending == "ar":
                return stem + "amos"
            else:
                return stem + "imos"
        case "vosotros":
            if verb.ending == "ar":
                return stem + "asteis"
            else:
                return stem + "isteis"
        case "ellos/ellas/Uds.":
            if verb.ending == "ar":
                return stem + "aron"
            else:
                return stem + "ieron"


def conjugate_imperfect(verb, pronoun):
    stem = verb.stem
    match pronoun:
        case "yo" | "él/ella/Ud.":
            if verb.ending == "ar":
                return stem + "aba"
            else:
                return stem + "ía"
        case "tú":
            if verb.ending == "ar":
                return stem + "abas"
            else:
                return stem + "ías"
        case "nosotros":
            if verb.ending == "ar":
                return stem + "ábamos"
            else:
                return stem + "íamos"
        case "vosotros":
            if verb.ending == "ar":
                return stem + "abais"
            else:
                return stem + "íais"
        case "ellos/ellas/Uds.":
            if verb.ending == "ar":
                return stem + "aban"
            else:
                return stem + "ían"


def conjugate_conditional(verb, pronoun):
    infinitive = verb.infinitive
    match pronoun:
        case "yo" | "él/ella/Ud.":
            return infinitive + "ía"
        case "tú":
            return infinitive + "ías"
        case "nosotros":
            return infinitive + "íamos"
        case "vosotros":
            return infinitive + "íais"
        case "ellos/ellas/Uds.":
            return infinitive + "ían"


def conjugate_future(verb, pronoun):
    infinitive = verb.infinitive
    match pronoun:
        case "yo":
            return infinitive + "é"
        case "tú":
            return infinitive + "ás"
        case "él/ella/Ud.":
            return infinitive + "á"
        case "nosotros":
            return infinitive + "emos"
        case "vosotros":
            return infinitive + "éis"
        case "ellos/ellas/Uds.":
            return infinitive + "án"
