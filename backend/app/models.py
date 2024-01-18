from . import db


class IrregularVerb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    infinitive = db.Column(db.String, nullable=False)
    conjugations = db.relationship('Conjugation', backref='irregular_verb', lazy=True)

    def __repr__(self):
        return f'<IrregularVerb {self.infinitive}>'


class RegularVerb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    infinitive = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<RegularVerb {self.infinitive}>'


class Tense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    conjugations = db.relationship('Conjugation', backref='tense', lazy=True)

    def __repr__(self):
        return f'<Tense {self.name}>'


class Conjugation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    verb_id = db.Column(db.Integer, db.ForeignKey('irregular_verb.id'), nullable=False)
    tense_id = db.Column(db.Integer, db.ForeignKey('tense.id'), nullable=False)
    first_s = db.Column(db.String, nullable=True)
    second_s = db.Column(db.String, nullable=True)
    third_s = db.Column(db.String, nullable=True)
    first_p = db.Column(db.String, nullable=True)
    second_p = db.Column(db.String, nullable=True)
    third_p = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'<Conjugation {self.verb.infinitive} {self.tense.name}>'
