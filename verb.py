class Verb:
    def __init__(self, infinitive):
        self._infinitive = infinitive

    def __str__(self):
        return self._infinitive

    @property
    def infinitive(self):
        return self._infinitive

    @property
    def stem(self):
        return self.get_verb_stem()

    @property
    def ending(self):
        return self.get_verb_ending()

    def get_verb_stem(self):
        return self._infinitive[:-2]

    def get_verb_ending(self):
        endings = ["ar", "er", "ir"]
        if self._infinitive[-2:] in endings:
            return self._infinitive[-2:]
