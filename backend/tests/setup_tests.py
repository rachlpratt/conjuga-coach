import os

from flask import Flask

from backend.app.extensions import db
from backend.app.models import RegularVerb, IrregularVerb, Tense, Conjugation
from backend.irregular_verbs import irregular_verbs


def setup_testing_db(cls):
    """Set up testing database."""
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))
    cls.app = Flask(__name__, instance_relative_config=True,
                    instance_path=os.path.join(base_dir, 'instance'))
    cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing_db.db'
    cls.app.config['TESTING'] = True
    db.init_app(cls.app)

    with cls.app.app_context():
        db.create_all()

        # Add irregular testing verbs to testing database
        irregular_testing_verbs = ["hacer", "ser", "decir", "ir"]
        for verb_infinitive in irregular_testing_verbs:
            testing_verb = IrregularVerb(infinitive=verb_infinitive)
            db.session.add(testing_verb)

        # Add regular testing verbs to testing database
        regular_testing_verbs = ["hablar", "beber", "vivir"]
        for verb_infinitive in regular_testing_verbs:
            testing_verb = RegularVerb(infinitive=verb_infinitive)
            db.session.add(testing_verb)

        # Add tenses to testing database
        testing_tenses = ["present", "preterite", "imperfect",
                          "conditional", "future", "present_subjunctive",
                          "imperfect_subjunctive_ra",
                          "imperfect_subjunctive_se",
                          "affirmative_imperative", "negative_imperative",
                          "participles"]
        for tense in testing_tenses:
            testing_tense = Tense(name=tense)
            db.session.add(testing_tense)

        # Add irregular conjugations to testing database
        for verb_infinitive, tenses in irregular_verbs.items():
            verb = IrregularVerb.query.filter_by(
                infinitive=verb_infinitive).first()
            if not verb:
                continue

            for tense_name, conjugations in tenses.items():
                tense = Tense.query.filter_by(name=tense_name).first()
                if tense_name == 'participles':
                    participle_conjugation = Conjugation(
                        verb_id=verb.id,
                        tense_id=tense.id,
                        present_participle=conjugations[0],
                        past_participle=conjugations[1]
                    )
                    db.session.add(participle_conjugation)
                else:
                    conjugation = Conjugation(
                        verb_id=verb.id,
                        tense_id=tense.id,
                        first_s=conjugations[0],
                        second_s=conjugations[1],
                        third_s=conjugations[2],
                        first_p=conjugations[3],
                        second_p=conjugations[4],
                        third_p=conjugations[5],
                    )
                    db.session.add(conjugation)

        db.session.commit()
