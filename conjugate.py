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
