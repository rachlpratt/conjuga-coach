class QuizItem:
    def __init__(self, question, answer):
        # The question will be a tuple containing a Verb object, tense, and pronoun
        # The answer will be the conjugated form
        self._question_verb = question[0]
        self._question_tense = question[1]
        self._question_pronoun = question[2]
        self._answer = answer

    @property
    def question_verb(self):
        return self._question_verb

    @property
    def question_tense(self):
        return self._question_tense

    @property
    def question_pronoun(self):
        return self._question_pronoun

    @property
    def answer(self):
        return self._answer
